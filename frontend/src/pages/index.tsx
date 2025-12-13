import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import RobotAnimation from '@site/src/components/RobotAnimation';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className={styles.heroContainer}>
        {/* Text Content */}
        <div className={styles.heroContent}>
          <Heading as="h1" className="hero__title">
            Physical AI & Humanoid Robotics
          </Heading>
          <p className="hero__subtitle">An Interactive, AI-Native Textbook</p>
          <p className={styles.heroDescription}>
            Master the future of robotics with hands-on simulations,
            cutting-edge AI techniques, and step-by-step guidance.
          </p>
          <div className={styles.buttons}>
            <Link
              className="button button--secondary button--lg"
              to="/chapter-01-intro/1.1-philosophy">
              Start Learning →
            </Link>
            <Link
              className={styles.secondaryButton}
              to="/chapter-01-intro/1.1-philosophy">
              View Chapters
            </Link>
          </div>
        </div>

        {/* Robot Animation */}
        <div className={styles.heroRobot}>
          <RobotAnimation />
        </div>
      </div>
    </header>
  );
}

function WhyPhysicalAI() {
  return (
    <section className={styles.whySection}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          Why Physical AI?
        </Heading>
        <p className={styles.sectionSubtitle}>
          The next frontier of artificial intelligence is embodied in the real world
        </p>

        <div className={styles.statsContainer}>
          <div className={styles.statCard}>
            <span className={styles.statNumber}>$38B</span>
            <span className={styles.statLabel}>Robotics Market by 2030</span>
          </div>
          <div className={styles.statCard}>
            <span className={styles.statNumber}>10x</span>
            <span className={styles.statLabel}>Growth in Humanoid Robots</span>
          </div>
          <div className={styles.statCard}>
            <span className={styles.statNumber}>100+</span>
            <span className={styles.statLabel}>Companies Building Humanoids</span>
          </div>
        </div>
      </div>
    </section>
  );
}

function TechStack() {
  const technologies = [
    { name: 'Python', color: '#3776AB' },
    { name: 'MuJoCo', color: '#00D9FF' },
    { name: 'PyTorch', color: '#EE4C2C' },
    { name: 'OpenAI', color: '#412991' },
    { name: 'JAX', color: '#7C3AED' },
    { name: 'Isaac Sim', color: '#76B900' },
  ];

  return (
    <section className={styles.techSection}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          Technologies You'll Learn
        </Heading>
        <div className={styles.techGrid}>
          {technologies.map((tech, idx) => (
            <div key={idx} className={styles.techItem} style={{ '--tech-color': tech.color } as React.CSSProperties}>
              <span>{tech.name}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function CTASection() {
  return (
    <section className={styles.ctaSection}>
      <div className="container">
        <Heading as="h2" className={styles.ctaTitle}>
          Ready to Build the Future?
        </Heading>
        <p className={styles.ctaSubtitle}>
          Start your journey into Physical AI and humanoid robotics today
        </p>
        <Link
          className={styles.ctaButton}
          to="/chapter-01-intro/1.1-philosophy">
          Begin Chapter 1 →
        </Link>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title="Physical AI & Humanoid Robotics"
      description="An interactive, AI-native textbook for learning physical AI and humanoid robotics">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <WhyPhysicalAI />
        <TechStack />
        <CTASection />
      </main>
    </Layout>
  );
}
