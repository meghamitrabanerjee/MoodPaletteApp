import streamlit as st
from palette_generator import generate_palette

# Ultimate CSS Styling for Glow, Animations & 3D Effects
st.markdown("""
    <style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Poppins:wght@300;400;600;700&display=swap');

/* Background - Enhanced Gradient Animation with Added Blue Shades */
@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background: linear-gradient(-45deg, #0a0d17, #1a103b, #231942, #120b29, #0f1b38, #142552, #1e3a8a, #312e81);
    background-size: 400% 400%;
    animation: gradientFlow 15s ease infinite;
    font-family: 'Outfit', sans-serif !important;
}

/* Title Styling with Enhanced 3D Effect */
@keyframes titleEntrance {
    0% { opacity: 0; transform: translateY(-30px) rotateX(10deg); }
    25% { opacity: 0.5; transform: translateY(-15px) rotateX(5deg); }
    100% { opacity: 1; transform: translateY(0) rotateX(0deg); }
}

.title {
    text-align: center;
    font-size: 52px;
    font-weight: 700;
    background: linear-gradient(to right, #ffffff, #c7d2fe, #ffffff);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-family: 'Poppins', sans-serif !important;
    text-shadow: 0px 0px 30px rgba(147, 51, 234, 0.7), 0px 5px 15px rgba(0, 0, 0, 0.3);
    margin-bottom: 25px;
    animation: titleEntrance 1.5s ease-out;
    letter-spacing: 2px;
    transform-style: preserve-3d;
    perspective: 1000px;
}

/* Subtitle styling with motion blur effect */
@keyframes subtitleGlow {
    0% { text-shadow: 0 0 5px rgba(165, 180, 252, 0.3); }
    50% { text-shadow: 0 0 15px rgba(165, 180, 252, 0.7); }
    100% { text-shadow: 0 0 5px rgba(165, 180, 252, 0.3); }
}

.subtitle {
    text-align: center;
    font-size: 19px;
    color: #a5b4fc;
    margin-bottom: 35px;
    font-weight: 300;
    animation: titleEntrance 1.8s ease-out, subtitleGlow 3s infinite ease-in-out;
    letter-spacing: 0.5px;
}

/* Content Card Styling with Frosted Glass Effect */
@keyframes cardEntrance {
    0% { opacity: 0; transform: translateY(30px) scale(0.95); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}

.content-card {
    background: rgba(30, 27, 75, 0.35);
    border-radius: 20px;
    padding: 30px;
    margin: 25px 0;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(139, 92, 246, 0.2);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.35), 0 0 25px rgba(139, 92, 246, 0.15);
    animation: cardEntrance 1.2s cubic-bezier(0.2, 0.8, 0.2, 1);
    transform-style: preserve-3d;
    transition: all 0.4s ease;
}

.content-card:hover {
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 30px rgba(139, 92, 246, 0.2);
    transform: translateY(-5px);
}

/* Mood Text Styling with Pulse Effect */
@keyframes moodPulse {
    0% { box-shadow: 0 0 10px rgba(139, 92, 246, 0.3); }
    50% { box-shadow: 0 0 20px rgba(139, 92, 246, 0.6); }
    100% { box-shadow: 0 0 10px rgba(139, 92, 246, 0.3); }
}

.mood-text {
    font-size: 30px;
    font-weight: 600;
    color: #f1f5f9;
    animation: titleEntrance 1.2s ease-out, moodPulse 3s infinite ease-in-out;
    background: rgba(76, 29, 149, 0.35);
    padding: 14px 28px;
    border-radius: 16px;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    display: inline-block;
    box-shadow: 0 5px 20px rgba(139, 92, 246, 0.35);
    border: 1px solid rgba(139, 92, 246, 0.35);
    margin-bottom: 25px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.mood-text::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
    transform: rotate(30deg);
}

.mood-text:hover::before {
    opacity: 1;
    animation: shimmerEffect 2s infinite;
}

@keyframes shimmerEffect {
    0% { transform: rotate(30deg) translateX(-100%); }
    100% { transform: rotate(30deg) translateX(100%); }
}

/* Palette Container with 3D Carousel Effect */
@keyframes containerFadeIn {
    0% { opacity: 0; transform: rotateY(10deg) translateZ(-50px); }
    100% { opacity: 1; transform: rotateY(0) translateZ(0); }
}

.palette-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: nowrap;
    margin-top: 30px;
    animation: containerFadeIn 1.5s ease-out;
    perspective: 1200px;
    transform-style: preserve-3d;
    overflow-x: auto;
    padding: 20px 5px;
    position: relative;
}

.palette-container::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 10%;
    width: 80%;
    height: 1px;
    background: linear-gradient(90deg, 
        rgba(139, 92, 246, 0), 
        rgba(139, 92, 246, 0.5), 
        rgba(139, 92, 246, 0));
}

/* Color Block Styling with Enhanced 3D Effect */
@keyframes floatAnimation {
    0% { transform: translateY(0px) rotateX(0deg) rotateZ(0deg); }
    50% { transform: translateY(-8px) rotateX(5deg) rotateZ(1deg); }
    100% { transform: translateY(0px) rotateX(0deg) rotateZ(0deg); }
}

@keyframes colorGlow {
    0% { box-shadow: 0 8px 20px rgba(0,0,0,0.3), 0 0 0px rgba(147, 51, 234, 0.3); }
    50% { box-shadow: 0 8px 30px rgba(0,0,0,0.4), 0 0 20px rgba(147, 51, 234, 0.6); }
    100% { box-shadow: 0 8px 20px rgba(0,0,0,0.3), 0 0 0px rgba(147, 51, 234, 0.3); }
}

.color-block {
    width: 110px;
    height: 110px;
    border-radius: 18px;
    border: 2px solid rgba(255,255,255,0.3);
    box-shadow: 0 12px 25px rgba(0,0,0,0.3), inset 0 0 20px rgba(255,255,255,0.1);
    margin: 12px 18px;
    display: inline-block;
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    animation: colorGlow 3s infinite ease-in-out;
    transform-style: preserve-3d;
    backface-visibility: hidden;
}

.color-block:hover {
    transform: scale(1.2) translateY(-15px) rotateY(10deg);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 30px rgba(147, 51, 234, 0.7);
    z-index: 10;
    animation: floatAnimation 2.5s infinite ease-in-out;
}

.color-block::before {
    content: "";
    position: absolute;
    top: -100%;
    left: -100%;
    width: 300%;
    height: 300%;
    background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
    transform: rotate(30deg);
}

.color-block:hover::before {
    opacity: 1;
    animation: rotateLight 3s infinite linear;
}

@keyframes rotateLight {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Color Hex Display with 3D Flip Effect */
@keyframes hexDisplay {
    0% { transform: rotateX(90deg); opacity: 0; }
    100% { transform: rotateX(0deg); opacity: 1; }
}

.color-hex-container {
    position: absolute;
    bottom: -35px;
    left: 0;
    width: 100%;
    text-align: center;
    opacity: 0;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    color: white;
    font-size: 13px;
    font-weight: 600;
    transform: rotateX(90deg);
    transform-origin: top center;
    text-shadow: 0 1px 3px rgba(0,0,0,0.8);
    letter-spacing: 0.5px;
}

.color-block:hover .color-hex-container {
    opacity: 1;
    bottom: 8px;
    text-shadow: 0 0 8px rgba(0,0,0,0.8);
    animation: hexDisplay 0.3s forwards;
}

/* Sidebar Glassmorphism with Light Effect */
@keyframes sidebarLight {
    0% { background-position: 0% 0%; }
    100% { background-position: 200% 200%; }
}
@keyframes sidebarPulse {
    0% { box-shadow: 0 0 0 rgba(139, 92, 246, 0.4), 0 0 20px rgba(139, 92, 246, 0.2); }
    50% { box-shadow: 0 0 30px rgba(139, 92, 246, 0.7), 0 0 40px rgba(139, 92, 246, 0.4); }
    100% { box-shadow: 0 0 0 rgba(139, 92, 246, 0.4), 0 0 20px rgba(139, 92, 246, 0.2); }
}

@keyframes arrowBounce {
    0%, 20%, 50%, 80%, 100% { transform: translateX(0); }
    40% { transform: translateX(-10px); }
    60% { transform: translateX(-5px); }
}

/* Sidebar Enhanced Styling with Animation */
section[data-testid="stSidebar"] {
    background: rgba(15, 11, 36, 0.7) !important;
    background-image: radial-gradient(circle at 100% 100%, rgba(139, 92, 246, 0.15) 0%, transparent 60%),
                      radial-gradient(circle at 0% 0%, rgba(139, 92, 246, 0.15) 0%, transparent 60%) !important;
    background-size: 200% 200%;
    animation: sidebarLight 15s linear infinite, sidebarPulse 3s infinite ease-in-out;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    color: white !important;
    padding: 28px 22px;
    border-radius: 24px;
    border: 1px solid rgba(139, 92, 246, 0.35);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25), inset 0 0 30px rgba(139, 92, 246, 0.05);
    transition: all 0.5s ease;
    position: relative;
}

/* Sidebar Guide - Floating Arrow and Text */
section[data-testid="stSidebar"]::before {
    content: "Select Mood Here";
    position: absolute;
    bottom: 50%;
    right: -180px;
    background: linear-gradient(135deg, #4338ca, #7e22ce, #9333ea);
    color: white;
    padding: 10px 15px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 16px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    z-index: 1000;
    opacity: 0.9;
    animation: arrowBounce 2s infinite;
    pointer-events: none;
    white-space: nowrap;
    transition: opacity 0.5s ease;
}

/* Hide guide after user interaction */
section[data-testid="stSidebar"]:hover::before {
    opacity: 0;
    animation: none;
    transition: opacity 0.3s ease;
}

/* Make sidebar more prominent */
section[data-testid="stSidebar"]:hover {
    box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3), inset 0 0 40px rgba(139, 92, 246, 0.2);
    transform: translateX(5px);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 22px;
}

/* Sidebar Header with Enhanced Shimmer Effect */
@keyframes headerShimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.css-10trblm {
    color: #c4b5fd !important;
    font-weight: 600;
    letter-spacing: 1px;
    position: relative;
    background: linear-gradient(90deg, #c4b5fd, #ffffff, #c4b5fd);
    background-size: 200% auto;
    -webkit-background-clip: text;
    background-clip: text;
    text-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
    animation: headerShimmer 3s linear infinite;
}

/* Selectbox Styling with Neon Effect - FIXED DROPDOWN DISPLAY ISSUE */
@keyframes selectboxPulse {
    0% { box-shadow: 0 0 5px rgba(139, 92, 246, 0.3); }
    50% { box-shadow: 0 0 15px rgba(139, 92, 246, 0.5); }
    100% { box-shadow: 0 0 5px rgba(139, 92, 246, 0.3); }
}

/* Fix for dropdown menu display issue */
/* Selectbox Styling */
.stSelectbox > div > div {
    background: rgba(76, 29, 149, 0.2) !important;
    border: 1px solid rgba(139, 92, 246, 0.3) !important;
    border-radius: 8px !important;
    color: white !important;
    transition: all 0.3s ease;
}

.stSelectbox > div > div:hover {
    border: 1px solid rgba(139, 92, 246, 0.6) !important;
    box-shadow: 0 0 15px rgba(139, 92, 246, 0.2);
}

/* Ensure dropdown options are visible */
div[data-baseweb="popover"] {
    z-index: 1000 !important;
}

div[data-baseweb="select"] {
    z-index: 100 !important;
}

/* Style for dropdown options */
div[data-baseweb="menu"] {
    background-color: rgba(30, 27, 75, 0.9) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(139, 92, 246, 0.3) !important;
    border-radius: 10px !important;
    margin-top: 5px !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4) !important;
}

div[role="option"] {
    color: white !important;
    transition: all 0.3s ease !important;
}

div[role="option"]:hover {
    background-color: rgba(139, 92, 246, 0.3) !important;
}

.stSelectbox > div > div:hover {
    border: 1px solid rgba(139, 92, 246, 0.7) !important;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.3), inset 0 0 10px rgba(139, 92, 246, 0.1);
    transform: translateY(-3px);
}

/* Ensure the select input has enough space */
.stSelectbox input {
    padding-bottom: 8px !important;
}

/* Button with Enhanced 3D and Holographic Effect */
@keyframes buttonGlow {
    0% { box-shadow: 0 0 15px rgba(147, 51, 234, 0.5); }
    50% { box-shadow: 0 0 30px rgba(147, 51, 234, 0.8), 0 0 15px rgba(255,255,255,0.3); }
    100% { box-shadow: 0 0 15px rgba(147, 51, 234, 0.5); }
}

@keyframes buttonLight {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stButton > button {
    font-size: 18px;
    font-weight: 600;
    padding: 14px 32px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg, #4338ca, #7e22ce, #9333ea);
    background-size: 300% 300%;
    animation: buttonLight 5s ease infinite;
    color: white;
    box-shadow: 0 5px 25px rgba(147, 51, 234, 0.5);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 15px;
    position: relative;
    overflow: hidden;
    transform: translateZ(0);
}

.stButton > button::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 60%);
    opacity: 0;
    transition: opacity 0.3s ease;
    transform: rotate(30deg);
    pointer-events: none;
}

.stButton > button:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 10px 30px rgba(147, 51, 234, 0.7), 0 0 30px rgba(147, 51, 234, 0.4);
    animation: buttonGlow 1.5s infinite alternate ease-in-out;
}

.stButton > button:hover::after {
    opacity: 1;
    animation: buttonSweep 2s infinite;
}

@keyframes buttonSweep {
    0% { transform: rotate(30deg) translateX(-100%); }
    100% { transform: rotate(30deg) translateX(100%); }
}

.stButton > button:active {
    transform: translateY(0px) scale(0.98);
    box-shadow: 0 5px 15px rgba(147, 51, 234, 0.5);
}

/* Code Blocks Styling with Terminal Effect */
@keyframes codeBlink {
    0%, 100% { border-color: rgba(139, 92, 246, 0.3); }
    50% { border-color: rgba(139, 92, 246, 0.7); }
}

.stCodeBlock {
    background: rgba(30, 27, 75, 0.8) !important;
    border: 1px solid rgba(139, 92, 246, 0.25);
    border-radius: 12px;
    padding: 18px;
    color: #a5f3fc !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25), inset 0 0 20px rgba(0, 0, 0, 0.3);
    font-family: 'Courier New', monospace;
    animation: codeBlink 3s infinite ease-in-out;
    position: relative;
    overflow: hidden;
}

.stCodeBlock::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #4338ca, #7e22ce, #9333ea);
    opacity: 0.7;
}

/* Error Message Styling with Pulse Effect */
@keyframes errorPulse {
    0% { background-color: rgba(239, 68, 68, 0.2); }
    50% { background-color: rgba(239, 68, 68, 0.3); }
    100% { background-color: rgba(239, 68, 68, 0.2); }
}

.stAlert {
    background: rgba(239, 68, 68, 0.2) !important;
    border: 1px solid rgba(239, 68, 68, 0.5);
    color: #fecaca !important;
    border-radius: 12px;
    padding: 12px 18px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15), 0 0 10px rgba(239, 68, 68, 0.2);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    animation: errorPulse 2s infinite ease-in-out;
    transform-style: preserve-3d;
}

/* Hex Code Label with Neon Glow */
@keyframes labelGlow {
    0% { text-shadow: 0 0 5px rgba(196, 181, 253, 0.5); }
    50% { text-shadow: 0 0 15px rgba(196, 181, 253, 0.8), 0 0 5px rgba(139, 92, 246, 0.5); }
    100% { text-shadow: 0 0 5px rgba(196, 181, 253, 0.5); }
}

.hex-code-label {
    font-size: 22px;
    color: #c4b5fd;
    font-weight: 600;
    margin-top: 35px;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 2px;
    background: rgba(76, 29, 149, 0.25);
    padding: 10px 18px;
    border-radius: 10px;
    display: inline-block;
    animation: labelGlow 3s infinite ease-in-out;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(139, 92, 246, 0.3);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2), 0 0 10px rgba(139, 92, 246, 0.2);
}

.hex-code-label::after {
    content: "";
    position: absolute;
    top: -100%;
    left: -100%;
    width: 300%;
    height: 300%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.hex-code-label:hover::after {
    opacity: 1;
    animation: rotateLight 3s infinite linear;
}

/* Scrollbar styling with Neon Effect */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(30, 27, 75, 0.3);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #4338ca, #7e22ce, #9333ea);
    border-radius: 10px;
    border: 2px solid rgba(30, 27, 75, 0.3);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #4338ca, #9333ea);
    box-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
}

/* Enhanced Animations */
@keyframes fadeOut {
    0% { opacity: 1; transform: scale(1); }
    100% { opacity: 0; transform: scale(0.95); }
}

@keyframes fadeIn {
    0% { opacity: 0; transform: scale(0.95); }
    100% { opacity: 1; transform: scale(1); }
}

.fade-out {
    animation: fadeOut 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}

.fade-in {
    animation: fadeIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}

@keyframes slideInLeft {
    0% { transform: translateX(-100%) scale(0.9) rotateY(10deg); opacity: 0; }
    100% { transform: translateX(0) scale(1) rotateY(0deg); opacity: 1; }
}

@keyframes slideInRight {
    0% { transform: translateX(100%) scale(0.9) rotateY(-10deg); opacity: 0; }
    100% { transform: translateX(0) scale(1) rotateY(0deg); opacity: 1; }
}

.color-block:nth-child(odd) {
    animation: slideInLeft 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}

.color-block:nth-child(even) {
    animation: slideInRight 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.shimmer-text {
    background: linear-gradient(90deg, #ffffff, #c7d2fe, #ffffff);
    background-size: 200% auto;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: shimmer 3s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg) scale(1); }
    50% { transform: rotate(180deg) scale(1.1); }
    100% { transform: rotate(360deg) scale(1); }
}

.loading-spinner {
    border: 4px solid rgba(255, 255, 255, 0.2);
    border-radius: 50%;
    border-top: 4px solid #9333ea;
    border-right: 4px solid transparent;
    border-bottom: 4px solid #4338ca;
    border-left: 4px solid transparent;
    width: 45px;
    height: 45px;
    animation: spin 1.2s cubic-bezier(0.5, 0.1, 0.5, 0.9) infinite;
    filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.5));
}

/* Background Flowing Animation - Blue + Purple Particles */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: 
        radial-gradient(circle at 20% 30%, rgba(56, 189, 248, 0.2) 0%, transparent 30%),
        radial-gradient(circle at 80% 40%, rgba(79, 70, 229, 0.25) 0%, transparent 35%),
        radial-gradient(circle at 40% 80%, rgba(16, 118, 190, 0.2) 0%, transparent 35%),
        radial-gradient(circle at 70% 90%, rgba(139, 92, 246, 0.2) 0%, transparent 35%);
    animation: backgroundShift 20s ease-in-out infinite alternate;
    z-index: -1;
    opacity: 0.9;
}

@keyframes backgroundShift {
    0% { background-position: 0% 0%; }
    50% { background-position: 25% 25%; }
    100% { background-position: 0% 0%; }
}

/* Flowing particles effect - ENHANCED */
@keyframes particleMove {
    0% { transform: translateY(0) translateX(0); opacity: 0; }
    50% { opacity: 0.7; }
    100% { transform: translateY(-100vh) translateX(20vw); opacity: 0; }
}

.stApp::after {
    content: "";
    position: fixed;
    bottom: -10px;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: 
        radial-gradient(circle at 10% 100%, rgba(56, 189, 248, 0.3) 0%, transparent 25%),
        radial-gradient(circle at 30% 100%, rgba(79, 70, 229, 0.25) 0%, transparent 30%),
        radial-gradient(circle at 70% 100%, rgba(16, 118, 190, 0.3) 0%, transparent 25%),
        radial-gradient(circle at 90% 100%, rgba(139, 92, 246, 0.25) 0%, transparent 30%);
    background-size: 200% 200%;
    animation: particleMove 15s ease-in-out infinite;
    z-index: -1;
    opacity: 0.7;
}

</style>
""", unsafe_allow_html=True)



# Title with Fade-In Animation
st.markdown("<h1 class='title'>Mood-Based Color Palette Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Create stunning color combinations that match your emotions</p>", unsafe_allow_html=True)


# Define 20 moods
MOODS = [
    "Happy", "Calm", "Romantic", "Mysterious", "Vintage", "Nature", "Dreamy", "Elegant", 
    "Fresh", "Festive", "Minimalist", "Sunset", "Ocean", "Space", "Retro", "Pastel",
    "Cinematic", "Neon", "Dark", "Soft"
]

# Streamlit Sidebar for Mood Selection
st.sidebar.title("Choose Your Mood")
mood = st.sidebar.selectbox("Select a mood:", MOODS)

# If the mood changes, reset the palette
if "selected_mood" not in st.session_state or st.session_state.selected_mood != mood:
    st.session_state.selected_mood = mood  # Update session state with new mood
    st.session_state.colors = generate_palette(mood)  # Generate a new palette for the new mood

colors = st.session_state.colors  # Get the stored colors

if colors:
    # Start content card
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    st.markdown(f"<p class='mood-text'>Mood: <b>{mood}</b></p>", unsafe_allow_html=True)
    st.write("**Generated Palette:**")

    # Display color blocks
    st.markdown('<div class="palette-container">', unsafe_allow_html=True)
    for color in colors:
        st.markdown(f'<div class="color-block' 
                    f'" style="background-color: {color};">'
                    f'<div class="color-hex-container">{color}</div></div>', 
                    unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Show HEX Codes
    st.markdown("<p class='hex-code-label'>HEX Codes:</p>", unsafe_allow_html=True)
    st.code(", ".join(colors))

    # Button to regenerate palette (placed inside content card now)
    if st.button("Generate Another Palette"):
        st.session_state.colors = generate_palette(st.session_state.selected_mood)  
        st.rerun()  # Updated method for rerunning

        
    # End content card
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.error(f"No palettes found for mood: {mood}")