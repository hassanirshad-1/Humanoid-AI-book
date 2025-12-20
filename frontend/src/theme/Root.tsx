import React from 'react';
import { TranslationProvider } from '../context/TranslationContext';
import TextSelectionTooltip from '../components/TextSelectionTooltip';
import BrowserOnly from '@docusaurus/BrowserOnly';
import Chat from '../components/Chat'; // Import the Chat component
import { SelectionProvider } from '../context/SelectionContext'; // Import SelectionProvider

interface RootProps {
    children: React.ReactNode;
}

// This is a Docusaurus theme wrapper component.
// It wraps the entire app to provide global context.
// See: https://docusaurus.io/docs/swizzling#wrapper-your-site-with-root

export default function Root({ children }: RootProps): JSX.Element {
    return (
        <SelectionProvider> {/* Wrap with SelectionProvider */}
            <TranslationProvider>
                {children}
                <BrowserOnly>
                    {() => (
                        <>
                            <TextSelectionTooltip />
                            <Chat /> {/* Render the Chat component */}
                        </>
                    )}
                </BrowserOnly>
            </TranslationProvider>
        </SelectionProvider>
    );
}