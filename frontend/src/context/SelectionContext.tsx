import React, { createContext, useState, useEffect, useCallback, useContext, ReactNode } from 'react';

interface SelectionContextType {
  selectedText: string;
  isChatOpen: boolean;
  clearSelection: () => void;
  setIsChatOpen: (open: boolean) => void;
}

const SelectionContext = createContext<SelectionContextType | undefined>(undefined);

interface SelectionProviderProps {
  children: ReactNode;
}

export const SelectionProvider: React.FC<SelectionProviderProps> = ({ children }) => {
  const [selectedText, setSelectedText] = useState<string>('');
  const [isChatOpen, setIsChatOpen] = useState<boolean>(false);

  const handleMouseUp = useCallback(() => {
    const selection = window.getSelection();
    const text = selection?.toString().trim();

    if (text && text.length > 0) {
      setSelectedText(text);
    } else {
      // If clicking inside a chat or tooltip, we might want to keep selection
      // but standard behavior is to clear on click.
      setSelectedText('');
    }
  }, []);

  useEffect(() => {
    document.addEventListener('mouseup', handleMouseUp);
    return () => {
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [handleMouseUp]);

  const clearSelection = () => {
    setSelectedText('');
  };

  return (
    <SelectionContext.Provider value={{ selectedText, isChatOpen, clearSelection, setIsChatOpen }}>
      {children}
    </SelectionContext.Provider>
  );
};

export const useSelection = () => {
  const context = useContext(SelectionContext);
  if (context === undefined) {
    throw new Error('useSelection must be used within a SelectionProvider');
  }
  return context;
};
