import React, {
    createContext,
    useContext,
    useState,
    useCallback,
    ReactNode,
    useRef,
} from 'react';

// No longer need content provider type as we use DOM directly
// type ContentProvider = () => string | null;

interface TranslationContextType {
    isTranslated: boolean;
    isLoading: boolean;
    originalContent: string | null;
    translatedContent: string | null;
    translatePage: () => Promise<void>;
    showOriginal: () => void;
    error: string | null;
    // registerContentProvider removed
}

const TranslationContext = createContext<TranslationContextType | undefined>(undefined);

const BACKEND_URL = 'http://localhost:8000';

interface TranslationProviderProps {
    children: ReactNode;
}

export function TranslationProvider({
    children,
}: TranslationProviderProps): React.ReactElement {
    const [isTranslated, setIsTranslated] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    // We store the original HTML string to revert back
    const [originalContent, setOriginalContent] = useState<string | null>(null);
    const [translatedContent, setTranslatedContent] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);

    // We primarily target the markdown article container
    const getArticleElement = () => document.querySelector('article');

    const translatePage = useCallback(async () => {
        const article = getArticleElement();
        if (!article) {
            console.error('Could not find article element to translate.');
            setError('Content not found.');
            return;
        }

        const currentHTML = article.innerHTML;
        if (!currentHTML.trim()) {
            setError('Page content is empty.');
            return;
        }

        setIsLoading(true);
        setError(null);
        article.classList.add('translation-scanning');

        // Make sure we have the original saved.
        // If we are already translated, we might want to avoid re-saving?
        // But translatePage should probably only be called if not isTranslated.
        if (!originalContent) {
            setOriginalContent(currentHTML);
        }

        try {
            // The backend service expects 'text', but our service handles HTML chunking.
            // So sending innerHTML is correct for our 'translate_text' service.
            const token = localStorage.getItem('bearer_token');
            const response = await fetch(`${BACKEND_URL}/api/translate`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    text: currentHTML,
                    target_language: 'Urdu',
                }),
            });

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({}));
                throw new Error(errorData.detail || `Translation failed: ${response.statusText}`);
            }

            const data = await response.json();
            const newContent = data.translated_text;

            setTranslatedContent(newContent);
            setIsTranslated(true);

            // Perform the DOM replacement
            article.innerHTML = newContent;

            // Since we replaced innerHTML, React might lose track of some event listeners 
            // attached to children, but for static content this is usually fine.
            // Docusaurus hydration might be tricky, but for reading purposes this works.

        } catch (err) {
            setError(err instanceof Error ? err.message : 'Translation failed');
            console.error('Translation error:', err);
        } finally {
            article.classList.remove('translation-scanning');
            setIsLoading(false);
        }
    }, [originalContent]);

    const showOriginal = useCallback(() => {
        const article = getArticleElement();
        if (article && originalContent) {
            article.innerHTML = originalContent;
        }
        setIsTranslated(false);
        // We keep translatedContent in state in case we want to toggle back instantly?
        // For now, let's allow re-translation.
    }, [originalContent]);

    const value: TranslationContextType = {
        isTranslated,
        isLoading,
        originalContent,
        translatedContent,
        translatePage,
        showOriginal,
        error,
    };

    return (
        <TranslationContext.Provider value={value}>{children}</TranslationContext.Provider>
    );
}

export function useTranslation(): TranslationContextType {
    const context = useContext(TranslationContext);
    if (context === undefined) {
        throw new Error('useTranslation must be used within a TranslationProvider');
    }
    return context;
}