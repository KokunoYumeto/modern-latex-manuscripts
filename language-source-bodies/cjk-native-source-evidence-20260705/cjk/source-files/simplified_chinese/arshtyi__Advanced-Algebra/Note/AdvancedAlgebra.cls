% ===========================================================================
% Mathematics Notebook Class
% A class file for mathematical notes and documents
% ===========================================================================

% --- Class Declaration ---
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{AdvancedAlgebra}

% --- Base Class and Options ---
\LoadClass[a4paper,12pt,twoside,openany]{book}

% ===========================================================================
% I. ENGINE DETECTION AND CORE PACKAGES
% ===========================================================================

% --- Engine Detection ---
\RequirePackage{ifxetex}
\RequireXeTeX % Requires XeTeX engine

% --- Core Programming Tools ---
\RequirePackage{etoolbox}    % Programming utilities for LaTeX

% --- PDF Support ---
\RequirePackage{ifpdf}
\ifpdf
    \RequirePackage{transparent}
\fi

% ===========================================================================
% II. LANGUAGE SUPPORT AND FONTS
% ===========================================================================

% --- CJK Support ---
\RequirePackage{ctex}        % Chinese language support

% --- Font Configuration ---
\setmainfont{Source Han Serif SC}[
    BoldFont=Source Han Serif SC Bold,
    ItalicFont=Source Han Serif SC Light,
    BoldItalicFont=Source Han Serif SC Bold
]

\setsansfont{Source Han Sans SC}[
    BoldFont=Source Han Sans SC Bold
]

\setmonofont{Consolas}[
    Scale=MatchLowercase
]

% ===========================================================================
% III. MATHEMATICS SUPPORT
% ===========================================================================

% --- Core Math Packages ---
\RequirePackage[tbtags]{amsmath}  % Advanced math environments
\RequirePackage{amsthm}           % Theorem environments
\RequirePackage{amsfonts}         % Math fonts (blackboard bold, etc.)
\RequirePackage{amssymb}          % Extended math symbols

% --- Extended Math Support ---
\RequirePackage{mathtools}        % Enhancements for amsmath
\RequirePackage{bm}               % Bold math symbols
\RequirePackage{extarrows}        % Extended arrow commands
% IV. GRAPHICS AND DIAGRAMS
% ===========================================================================

% --- TikZ and Diagram Support ---
\RequirePackage{tikz}             % Vector graphics system
\RequirePackage{tikz-cd}          % Commutative diagrams
\RequirePackage{tikzsymbols}      % Additional TikZ symbols

% ===========================================================================
% V. DOCUMENT STRUCTURE
% ===========================================================================

% --- Structure and Organization ---
\RequirePackage{appendix}         % Appendix formatting
\RequirePackage{environ}          % Environment creation tools

% ===========================================================================
% VI. HYPERLINKS AND REFERENCES
% ===========================================================================

% --- Hyperlink System ---
\RequirePackage[
    breaklinks,
    colorlinks,
    linkcolor=black,
    citecolor=black,
    urlcolor=red,
    bookmarksdepth=2,
    bookmarksnumbered=true,
    bookmarksopen=true
]{hyperref}

% --- Enhanced References ---
\RequirePackage{theoremref}                     % Theorem references
\RequirePackage[depth=2,open=true,numbered=true]{bookmark} % PDF bookmarks
\RequirePackage[nameinlink]{cleveref}           % Intelligent cross-references
\RequirePackage{nameref}                        % Reference by name

% ===========================================================================
% End of Class File
% ===========================================================================

\endinput
