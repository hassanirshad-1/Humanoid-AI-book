import React, { useEffect, useRef } from 'react';
import DocItem from '@theme-original/DocItem';
import type DocItemType from '@theme/DocItem';
import type { WrapperProps } from '@docusaurus/types';
import TranslateButton from '../../components/TranslateButton';
import BrowserOnly from '@docusaurus/BrowserOnly';

type Props = WrapperProps<typeof DocItemType>

function TranslationWrapper({ children }) {
    // We no longer need to register content provider or handle swapping here
    // The TranslationContext now handles this globally/via direct DOM access
    return (
        <div>
            <div style={{ marginBottom: '1rem', display: 'flex', justifyContent: 'flex-end' }}>
                <TranslateButton />
            </div>
            {children}
        </div>
    );
}

export default function DocItemWrapper(props: Props): JSX.Element {
    return (
        <BrowserOnly>
            {() => (
                <TranslationWrapper>
                    <DocItem {...props} />
                </TranslationWrapper>
            )}
        </BrowserOnly>
    );
}
