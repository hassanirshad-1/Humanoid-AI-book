import React, { useState, useEffect } from 'react';
import ChatUI from './ChatUI';
import styles from './styles.module.css';
import { useSelection } from '../../context/SelectionContext';

const Chat: React.FC = () => {
  const { isChatOpen, setIsChatOpen, selectedText, clearSelection } = useSelection();
  const [showLabel, setShowLabel] = useState(false);

  const toggleChat = () => {
    setIsChatOpen(!isChatOpen);
    setShowLabel(false); // Hide label when chat is interacted with
    // If chat is closed, we clear selection if it was opened from one
    if (isChatOpen && selectedText) {
      clearSelection();
    }
  };

  useEffect(() => {
    // Auto-show label after 3 seconds if chat is closed
    const timer = setTimeout(() => {
      if (!isChatOpen) {
        setShowLabel(true);
      }
    }, 3000);
    return () => clearTimeout(timer);
  }, [isChatOpen]);

  return (
    <>
      <button
        className={`${styles.chatButton} ${showLabel ? styles.labelActive : ''}`}
        onClick={toggleChat}
        aria-label="Toggle AI Tutor"
      >
        <div className={styles.chatButtonLabel}>Need Help? 👋</div>
        {isChatOpen ? (
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        ) : (
          /* Robot Bot Icon */
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,2A10,10,0,0,0,2,12a9.89,9.89,0,0,0,2.26,6.33l-2,2a1,1,0,0,0-.21,1.09A1,1,0,0,0,3,22h9a10,10,0,0,0,0-20Zm0,18H5.41l.29-.29a1,1,0,0,0,0-1.42l-1.1-1.1A8,8,0,1,1,12,20Z" />
            <path d="M7,12a1,1,0,1,0,1,1A1,1,0,0,0,7,12Z" />
            <path d="M17,12a1,1,0,1,0,1,1A1,1,0,0,0,17,12Z" />
            <rect x="9" y="15" width="6" height="2" rx="1" />
          </svg>
        )}
      </button>

      {isChatOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <div className={styles.chatHeaderTitle}>
              <div className={styles.onlineIndicator} />
              <span>AI Tutor</span>
            </div>
          </div>
          <ChatUI initialMessage={selectedText} />
        </div>
      )}
    </>
  );
};

export default Chat;