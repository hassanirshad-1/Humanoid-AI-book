import React from 'react';
import styles from './RobotAnimation.module.css';

export default function RobotAnimation(): React.ReactNode {
    return (
        <div className={styles.robotContainer}>
            {/* Floating particles */}
            <div className={styles.particles}>
                {[...Array(8)].map((_, i) => (
                    <div key={i} className={styles.particle} style={{
                        animationDelay: `${i * 0.5}s`,
                        left: `${10 + (i * 12)}%`
                    }} />
                ))}
            </div>

            {/* Glowing orb background */}
            <div className={styles.glowOrb} />
            <div className={styles.glowOrbSecondary} />

            {/* Animated Robot SVG */}
            <svg
                className={styles.robot}
                viewBox="0 0 200 280"
                xmlns="http://www.w3.org/2000/svg"
            >
                <defs>
                    <linearGradient id="robotBodyGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style={{ stopColor: '#00D9FF' }} />
                        <stop offset="100%" style={{ stopColor: '#7C3AED' }} />
                    </linearGradient>
                    <filter id="robotGlow">
                        <feGaussianBlur stdDeviation="4" result="coloredBlur" />
                        <feMerge>
                            <feMergeNode in="coloredBlur" />
                            <feMergeNode in="SourceGraphic" />
                        </feMerge>
                    </filter>
                    <filter id="innerGlow">
                        <feGaussianBlur stdDeviation="2" result="coloredBlur" />
                        <feMerge>
                            <feMergeNode in="coloredBlur" />
                            <feMergeNode in="SourceGraphic" />
                        </feMerge>
                    </filter>
                </defs>

                {/* Antenna */}
                <g className={styles.antenna}>
                    <line x1="100" y1="20" x2="100" y2="5" stroke="#00D9FF" strokeWidth="3" />
                    <circle cx="100" cy="5" r="5" fill="#7C3AED" filter="url(#robotGlow)">
                        <animate attributeName="opacity" values="0.5;1;0.5" dur="1.5s" repeatCount="indefinite" />
                    </circle>
                </g>

                {/* Head */}
                <g className={styles.head}>
                    {/* Head outline */}
                    <rect x="55" y="20" width="90" height="70" rx="15"
                        fill="none" stroke="url(#robotBodyGradient)" strokeWidth="3"
                        filter="url(#robotGlow)" />

                    {/* Face plate */}
                    <rect x="65" y="30" width="70" height="50" rx="10"
                        fill="rgba(0, 217, 255, 0.1)" stroke="#00D9FF" strokeWidth="1" />

                    {/* Eyes */}
                    <g className={styles.eyes}>
                        <ellipse cx="82" cy="52" rx="10" ry="12" fill="#0A0A1A" stroke="#00D9FF" strokeWidth="2" />
                        <ellipse cx="118" cy="52" rx="10" ry="12" fill="#0A0A1A" stroke="#00D9FF" strokeWidth="2" />
                        {/* Pupils with glow */}
                        <circle cx="82" cy="52" r="5" fill="#00D9FF" filter="url(#innerGlow)">
                            <animate attributeName="r" values="5;6;5" dur="2s" repeatCount="indefinite" />
                        </circle>
                        <circle cx="118" cy="52" r="5" fill="#00D9FF" filter="url(#innerGlow)">
                            <animate attributeName="r" values="5;6;5" dur="2s" repeatCount="indefinite" />
                        </circle>
                    </g>

                    {/* Mouth/visor */}
                    <rect x="75" y="70" width="50" height="8" rx="4" fill="url(#robotBodyGradient)" opacity="0.7">
                        <animate attributeName="opacity" values="0.5;0.9;0.5" dur="3s" repeatCount="indefinite" />
                    </rect>
                </g>

                {/* Neck */}
                <rect x="90" y="90" width="20" height="15" fill="none" stroke="#7C3AED" strokeWidth="2" />

                {/* Body */}
                <g className={styles.body}>
                    {/* Torso */}
                    <path d="M50 105 L150 105 L145 200 L55 200 Z"
                        fill="none" stroke="url(#robotBodyGradient)" strokeWidth="3"
                        filter="url(#robotGlow)" />

                    {/* Chest plate */}
                    <rect x="70" y="120" width="60" height="50" rx="8"
                        fill="rgba(124, 58, 237, 0.15)" stroke="#7C3AED" strokeWidth="1" />

                    {/* Core light */}
                    <circle cx="100" cy="145" r="15" fill="rgba(0, 217, 255, 0.2)" stroke="#00D9FF" strokeWidth="2">
                        <animate attributeName="r" values="15;18;15" dur="2s" repeatCount="indefinite" />
                    </circle>
                    <circle cx="100" cy="145" r="8" fill="#00D9FF" filter="url(#robotGlow)">
                        <animate attributeName="opacity" values="0.7;1;0.7" dur="1.5s" repeatCount="indefinite" />
                    </circle>
                </g>

                {/* Arms */}
                <g className={styles.leftArm}>
                    <path d="M50 110 L30 110 L25 150 L35 190"
                        fill="none" stroke="#00D9FF" strokeWidth="3" strokeLinecap="round" />
                    <circle cx="35" cy="190" r="8" fill="none" stroke="#7C3AED" strokeWidth="2" />
                </g>
                <g className={styles.rightArm}>
                    <path d="M150 110 L170 110 L175 150 L165 190"
                        fill="none" stroke="#00D9FF" strokeWidth="3" strokeLinecap="round" />
                    <circle cx="165" cy="190" r="8" fill="none" stroke="#7C3AED" strokeWidth="2" />
                </g>

                {/* Legs */}
                <g className={styles.legs}>
                    <path d="M70 200 L65 250 L55 265" fill="none" stroke="url(#robotBodyGradient)" strokeWidth="3" strokeLinecap="round" />
                    <path d="M130 200 L135 250 L145 265" fill="none" stroke="url(#robotBodyGradient)" strokeWidth="3" strokeLinecap="round" />
                    {/* Feet */}
                    <ellipse cx="55" cy="270" rx="12" ry="6" fill="none" stroke="#7C3AED" strokeWidth="2" />
                    <ellipse cx="145" cy="270" rx="12" ry="6" fill="none" stroke="#7C3AED" strokeWidth="2" />
                </g>

                {/* Circuit lines decoration */}
                <g opacity="0.4">
                    <path d="M145 130 L160 130 L160 160" stroke="#00D9FF" strokeWidth="1" />
                    <path d="M55 130 L40 130 L40 160" stroke="#00D9FF" strokeWidth="1" />
                    <circle cx="160" cy="160" r="3" fill="#EC4899" />
                    <circle cx="40" cy="160" r="3" fill="#EC4899" />
                </g>
            </svg>

            {/* Ground reflection */}
            <div className={styles.reflection} />
        </div>
    );
}
