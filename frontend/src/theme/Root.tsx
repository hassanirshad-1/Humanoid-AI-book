import React from 'react';
import { TranslationProvider } from '../context/TranslationContext';
import TextSelectionTooltip from '../components/TextSelectionTooltip';
import BrowserOnly from '@docusaurus/BrowserOnly';

interface RootProps {
    children: React.ReactNode;
}

// This is a Docusaurus theme wrapper component.
// It wraps the entire app to provide global context.
// See: https://docusaurus.io/docs/swizzling#wrapper-your-site-with-root

export default function Root({ children }: RootProps): JSX.Element {
    return (
        <TranslationProvider>
            {children}
            <BrowserOnly>
                {() => <TextSelectionTooltip />}
            </BrowserOnly>
        </TranslationProvider>
    );
}