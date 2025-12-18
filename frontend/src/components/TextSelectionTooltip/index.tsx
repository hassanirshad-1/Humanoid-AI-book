import React, { useState, useEffect, useCallback } from 'react';
import styles from './styles.module.css';

const BACKEND_URL = 'http://localhost:8000';

interface TooltipPosition {
    x: number;
    y: number;
}

export default function TextSelectionTooltip(): JSX.Element | null {
    const [selectedText, setSelectedText] = useState<string>('');
    const [position, setPosition] = useState<TooltipPosition | null>(null);
    const [translatedText, setTranslatedText] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleMouseUp = useCallback(() => {
        const selection = window.getSelection();
        const text = selection?.toString().trim();

        if (text && text.length > 0) {
            const range = selection?.getRangeAt(0);
            const rect = range?.getBoundingClientRect();

            if (rect) {
                setSelectedText(text);
                setPosition({
                    x: rect.left + rect.width / 2,
                    y: rect.top - 10,
                });
                setTranslatedText(null);
                setError(null);
            }
        } else {
            // Only hide if clicking outside the tooltip
            setTimeout(() => {
                const tooltip = document.querySelector(`.${styles.tooltip}`);
                if (!tooltip?.matches(':hover')) {
                    setSelectedText('');
                    setPosition(null);
                    setTranslatedText(null);
                }
            }, 100);
        }
    }, []);

    useEffect(() => {
        document.addEventListener('mouseup', handleMouseUp);
        return () => {
            document.removeEventListener('mouseup', handleMouseUp);
        };
    }, [handleMouseUp]);

    const handleTranslate = async () => {
        if (!selectedText) return;

        setIsLoading(true);
        setError(null);

        try {
            const response = await fetch(`${BACKEND_URL}/api/translate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: selectedText,
                    target_language: 'Urdu',
                }),
            });

            if (!response.ok) {
                throw new Error(`Translation failed: ${response.statusText}`);
            }

            const data = await response.json();
            setTranslatedText(data.translated_text);
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Translation failed');
        } finally {
            setIsLoading(false);
        }
    };

    const handleClose = () => {
        setSelectedText('');
        setPosition(null);
        setTranslatedText(null);
        setError(null);
    };

    if (!position || !selectedText) {
        return null;
    }

    return (
        <div
            className={styles.tooltip}
            style={{
                left: `${position.x}px`,
                top: `${position.y}px`,
            }}
        >
            <button className={styles.closeButton} onClick={handleClose} aria-label="Close">
                ×
            </button>

            {!translatedText && !isLoading && (
                <button className={styles.translateBtn} onClick={handleTranslate}>
                    🇵🇰 Translate to Urdu
                </button>
            )}

            {isLoading && (
                <div className={styles.loading}>
                    <span className={styles.spinner}></span>
                    Translating...
                </div>
            )}

            {error && <div className={styles.error}>{error}</div>}

            {translatedText && (
                <div className={styles.translationResult}>
                    <div className={styles.translationLabel}>Urdu Translation:</div>
                    <div className={styles.translatedText} dir="rtl" lang="ur">
                        {translatedText?.replace(/```html|```/g, '').replace(/<[^>]*>/g, '')}
                    </div>
                </div>
            )}
        </div>
    );
}
