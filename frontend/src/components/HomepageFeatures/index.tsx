import type { ReactNode } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Interactive & Hands-On',
    Svg: require('@site/static/img/icon-interactive.svg').default,
    description: (
      <>
        Learn by doing with runnable code examples, interactive simulations,
        and practical exercises. Every concept is reinforced with hands-on
        implementations you can experiment with.
      </>
    ),
  },
  {
    title: 'Modern & AI-Native',
    Svg: require('@site/static/img/icon-ai-native.svg').default,
    description: (
      <>
        Focus on cutting-edge AI techniques for robotics, not outdated classical
        methods. Built for the era of foundation models, imitation learning, and
        embodied AI.
      </>
    ),
  },
  {
    title: 'Built for Beginners',
    Svg: require('@site/static/img/icon-beginner.svg').default,
    description: (
      <>
        Progressive, step-by-step approach that takes you from zero to building
        your first humanoid robot. No prior robotics experience required—just
        curiosity and a willingness to learn.
      </>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
