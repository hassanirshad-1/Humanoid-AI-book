import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Manual sidebar for the textbook
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Chapter 0: Welcome',
      items: [
        'chapter-00-welcome/0.1-welcome',
        'chapter-00-welcome/0.2-prerequisites',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 1: Introduction',
      items: [
        'chapter-01-intro/1.1-philosophy',
        'chapter-01-intro/1.2-hardware-anatomy',
        'chapter-01-intro/1.3-simulation-setup',
        'chapter-01-intro/1.4-first-policy',
      ],
    },
  ],
};

export default sidebars;
