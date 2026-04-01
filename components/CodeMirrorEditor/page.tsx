'use client';

import React, { useCallback } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { markdown, markdownLanguage } from '@codemirror/lang-markdown';
import { languages } from '@codemirror/language-data';
import { EditorView, gutter } from '@codemirror/view';

// 1. THE OBSIDIAN THEME
// As per the "Styles and Themes" docs, we define a theme to override default styles.
const obsidianTheme = EditorView.theme({
  "&": {
    backgroundColor: "transparent !important", // No gray code background
    height: "100%",
  },
  ".cm-content": {
    caretColor: "#fff",    // White cursor
    fontFamily: "Inter, sans-serif", // Use a normal UI font, not monospace
    fontSize: "16px",
    padding: "0",          // Remove default padding
  },
  ".cm-gutters": {
    backgroundColor: "transparent !important" ,
    color: "#6c6c6c",
    border: 'none'      // 👈 HIDDEN: This removes the line numbers (1, 2, 3)
  },
  ".cm-line": {
    padding: "0 4px",      // Add slight breathing room
  },
  "&.cm-focused .cm-cursor": {
    borderLeftColor: "#fff"
  },
  ".cm-activeLineGutter": {
    backgroundColor: 'transparent !important',
    height: 'auto'
  },
  ".cm-foldPlaceholder": {
    backgroundColor: "transparent !important",
    border: "none"
  },
});

interface EditorProps {
  initialContent: string;
  onChange: (doc: string) => void;
}

export default function CodeMirrorEditor({ initialContent, onChange }: EditorProps) {
  
  // Memoize handler to prevent re-renders (Performance)
  const handleChange = useCallback((val: string) => {
    onChange(val);
  }, [onChange]);

  return (
    <div className="w-full h-full text-left" onMouseDown={(e) => e.stopPropagation()}>
      <CodeMirror
        value={initialContent}
        height="100%"
        theme={obsidianTheme} // Apply our custom theme
        
        // 2. EXTENSIONS
        // As per "Modularity" docs, we add the specific blocks we need.
        extensions={[
          markdown({ base: markdownLanguage, codeLanguages: languages }), // Markdown support
          EditorView.lineWrapping, // Wrap long lines like a note
          gutter({class: "cm-mygutter"})
        ]}
        
        onChange={handleChange}
        
        // 3. BASIC SETUP
        // We disable default code-editor features we don't want
        basicSetup={{
          lineNumbers: false,
          foldGutter: true,
          highlightActiveLine: false,
          drawSelection: true,
        }}
      />
    </div>
  );
}