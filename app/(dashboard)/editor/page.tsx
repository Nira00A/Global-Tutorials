'use client';

import React, { useState } from 'react';
import dynamic from 'next/dynamic';
import Link from 'next/link';

// 1. Lazy Load the Editor
// This ensures Next.js doesn't try to render CodeMirror on the server
const CodeMirrorEditor = dynamic(
  () => import('@/components/CodeMirrorEditor/page'), 
  { 
    ssr: false,
    loading: () => <div className="p-10 text-neutral-500">Loading editor...</div>
  }
);

export default function EditorPage() {
  const [content, setContent] = useState<string>("# Untitled Note\n\nStart typing here...");

  return (
    <div className="flex flex-col h-screen w-screen bg-[#111] text-white overflow-hidden">
      
      {/* --- Header / Toolbar --- */}
      <div className="h-12 border-b border-neutral-800 flex items-center px-4 justify-between bg-[#191919]">
        <div className="flex items-center gap-4">
          <Link href="/" className="text-sm text-neutral-400 hover:text-white transition-colors">
            ← Back
          </Link>
          <span className="text-sm font-medium text-neutral-200">Editor Test</span>
        </div>
        
        <div className="text-xs text-neutral-500">
          {content.length} characters
        </div>
      </div>

      {/* --- Main Editor Area --- */}
      {/* We give it flex-1 so it takes up all remaining vertical space */}
      <div className="flex-1 overflow-hidden relative">
        <div className="absolute inset-0 p-4 max-w-3xl mx-auto">
          <CodeMirrorEditor 
            initialContent={content} 
            onChange={(newDoc) => setContent(newDoc)} 
          />
        </div>
      </div>

    </div>
  );
}