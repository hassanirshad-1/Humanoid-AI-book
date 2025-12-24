import React from 'react';
import { TranslationProvider } from '../context/TranslationContext';
import { AuthProvider, useAuth } from '../context/AuthContext';
import TextSelectionTooltip from '../components/TextSelectionTooltip';
import BrowserOnly from '@docusaurus/BrowserOnly';
import Chat from '../components/Chat';
import { SelectionProvider } from '../context/SelectionContext';

interface RootProps {
    children: React.ReactNode;
}

function AuthenticatedContent({ children }: { children: React.ReactNode }) {
    const { isAuthenticated } = useAuth();

    return (
        <>
            {children}
            <BrowserOnly>
                {() => (
                    <>
                        <TextSelectionTooltip />
                        <Chat />
                    </>
                )}
            </BrowserOnly>
        </>
    );
}

export default function Root({ children }: RootProps): JSX.Element {
    return (
        <AuthProvider>
            <SelectionProvider>
                <TranslationProvider>
                    <AuthenticatedContent>
                        {children}
                    </AuthenticatedContent>
                </TranslationProvider>
            </SelectionProvider>
        </AuthProvider>
    );
}