import React from 'react';
import { useTranslation } from '../../context/TranslationContext';
import styles from './styles.module.css';

export default function TranslateButton(): JSX.Element | null {
    const { isTranslated, isLoading, translatePage, showOriginal, error } = useTranslation();

    const handleClick = () => {
        if (isTranslated) {
            showOriginal();
        } else {
            translatePage();
        }
    };

    return (
        <div className={styles.translateButtonContainer}>
            <button
                className={styles.translateButton}
                onClick={handleClick}
                disabled={isLoading}
                aria-label={isTranslated ? 'Show Original' : 'Translate to Urdu'}
            >
                {isLoading ? (
                    <>
                        <span className={styles.spinner}></span>
                        Translating...
                    </>
                ) : isTranslated ? (
                    <>🌐 Show Original</>
                ) : (
                    <>🇵🇰 Translate to Urdu</>
                )}
            </button>
            {error && <span className={styles.errorMessage}>{error}</span>}
        </div>
    );
}
