import React, { useState, useRef, useEffect } from 'react';
import styles from './styles.module.css';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css'; // Import KaTeX CSS

interface Message {
  id: string;
  sender: 'user' | 'ai';
  content: string;
}

interface ChatUIProps {
  initialMessage?: string;
}

const ChatUI: React.FC<ChatUIProps> = ({ initialMessage }) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = (behavior: ScrollBehavior = 'smooth') => {
    messagesEndRef.current?.scrollIntoView({ behavior });
  };

  useEffect(() => {
    // Only auto-scroll if there are messages (prevents scrolling to bottom on welcome screen)
    if (messages.length > 0) {
      const lastMessage = messages[messages.length - 1];
      // Use 'auto' for streaming updates, 'smooth' for everything else
      scrollToBottom(lastMessage?.sender === 'ai' && lastMessage.content !== 'Thinking...' ? 'auto' : 'smooth');
    }

    if (!sessionId) {
      // Generate a new session ID when the component mounts if it doesn't exist
      setSessionId(localStorage.getItem('chatSessionId') || Date.now().toString());
    }
  }, [messages, sessionId]);

  useEffect(() => {
    // Persist session ID to local storage
    if (sessionId) {
      localStorage.setItem('chatSessionId', sessionId);
    }
  }, [sessionId]);

  useEffect(() => {
    if (initialMessage) {
      setInput(initialMessage);
      // Optionally send the message immediately
      // handleSendMessage({ preventDefault: () => {} } as React.FormEvent); 
    }
  }, [initialMessage]); // Only re-run if initialMessage changes

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      const userMessage: Message = { id: Date.now().toString(), sender: 'user', content: input.trim() };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setInput('');

      // Add a placeholder for AI response
      const aiPlaceholder: Message = { id: (Date.now() + 1).toString(), sender: 'ai', content: 'Thinking...' };
      setMessages((prevMessages) => [...prevMessages, aiPlaceholder]);

      try {
        const response = await fetch('http://localhost:8000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            message: userMessage.content,
            context: {
              session_id: sessionId,
              current_url: window.location.href,
            },
          }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const reader = response.body?.getReader();
        const decoder = new TextDecoder('utf-8');
        let aiResponseContent = '';
        let done = false;

        while (!done && reader) {
          const { value, done: readerDone } = await reader.read();
          done = readerDone;
          const chunk = decoder.decode(value, { stream: true });

          // Process each SSE data chunk
          const lines = chunk.split('\n');
          for (const line of lines) {
            if (!line.trim()) continue;
            try {
              // Determine if it's JSON already or if it needs parsing logic
              // Our backend sends lines like: {"type": "data", "content": "..."}
              // (Standard SSE format usually requires data prefix, but our manual yield does json lines)

              // If the line is valid JSON, parse it
              const data = JSON.parse(line);

              if (data.type === 'data') {
                aiResponseContent += data.content;
              } else if (data.type === 'end') {
                if (data.session_id) setSessionId(data.session_id);
              } else if (data.type === 'error') {
                aiResponseContent = "Error: " + data.content;
              }

              // Update UI live
              setMessages((prevMessages) => {
                const updatedMessages = [...prevMessages];
                const lastAiMessageIndex = updatedMessages.findLastIndex((msg) => msg.sender === 'ai');
                if (lastAiMessageIndex !== -1) {
                  updatedMessages[lastAiMessageIndex].content = aiResponseContent;
                }
                return updatedMessages;
              });

            } catch (e) {
              // If it's standard SSE 'data: ' prefix, handle that too just in case
              if (line.startsWith('data: ')) {
                const jsonStr = line.substring(6);
                try {
                  const data = JSON.parse(jsonStr);
                  if (data.type === 'data') aiResponseContent += data.content;
                  // Trigger update
                  setMessages((prevMessages) => {
                    const updatedMessages = [...prevMessages];
                    const lastAiMessageIndex = updatedMessages.findLastIndex((msg) => msg.sender === 'ai');
                    if (lastAiMessageIndex !== -1) updatedMessages[lastAiMessageIndex].content = aiResponseContent;
                    return updatedMessages;
                  });
                } catch { }
              }
            }
          }
        }
      } catch (error) {
        console.error('Error sending message:', error);
        setMessages((prevMessages) => {
          // ... error handling logic
          const updated = [...prevMessages];
          const lastIdx = updated.findLastIndex(m => m.sender === 'ai');
          if (lastIdx !== -1) updated[lastIdx].content = "Sorry, I encountered an error connectnig to the Tutor.";
          return updated;
        });
      }
    }
  };

  const handleSuggestionClick = (suggestion: string) => {
    setInput(suggestion);
  };

  return (
    <>
      <div className={styles.messagesContainer}>
        {messages.length === 0 ? (
          <div className={styles.welcomeContainer}>
            <h3 className={styles.welcomeTitle}>Hello! I'm your AI Tutor</h3>
            <p className={styles.welcomeText}>
              I can help you understand humanoid robotics. Try one of these:
            </p>
            <div className={styles.suggestionsGrid}>
              {[
                "🔍 Explain this page",
                "💡 Key concepts here?",
                "📝 Quiz me on this content",
                "🧠 How do I start?"
              ].map((s) => (
                <button
                  key={s}
                  className={styles.suggestionChip}
                  onClick={() => handleSuggestionClick(s)}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg) => (
            <div key={msg.id} className={`${styles.message} ${styles[msg.sender]}`}>
              {msg.content === 'Thinking...' ? (
                <div className={styles.typingIndicator}>
                  <span></span><span></span><span></span>
                </div>
              ) : (
                <ReactMarkdown
                  remarkPlugins={[remarkMath]}
                  rehypePlugins={[rehypeKatex]}
                >
                  {msg.content}
                </ReactMarkdown>
              )}
            </div>
          ))
        )}
        <div ref={messagesEndRef} />
      </div>
      <form className={styles.inputForm} onSubmit={handleSendMessage}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          className={styles.textInput}
        />
        <button type="submit" className={styles.sendButton} disabled={!input.trim()}>
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
        </button>
      </form>
    </>
  );
};

export default ChatUI;
