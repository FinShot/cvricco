import React from 'react';
import type { PortableTextComponents } from '@portabletext/react';

// Define custom components for rendering Portable Text
export const portableTextComponents: PortableTextComponents = {
  marks: {
    link: ({ value, children }) => {
      const { href, blank } = value;
      return blank ? (
        <a href={href} target="_blank" rel="noopener noreferrer">
          {children}
        </a>
      ) : (
        <a href={href}>{children}</a>
      );
    },
  },
  block: {
    // You can customize how different block types are rendered
    normal: ({ children }) => <p>{children}</p>,
    h1: ({ children }) => <h1 className="text-2xl font-bold">{children}</h1>,
    h2: ({ children }) => <h2 className="text-xl font-bold">{children}</h2>,
    h3: ({ children }) => <h3 className="text-lg font-bold">{children}</h3>,
    blockquote: ({ children }) => <blockquote className="border-l-4 pl-4 italic">{children}</blockquote>,
  },
  list: {
    bullet: ({ children }) => <ul className="list-disc pl-5 my-2">{children}</ul>,
    number: ({ children }) => <ol className="list-decimal pl-5 my-2">{children}</ol>,
  },
  listItem: {
    bullet: ({ children }) => <li>{children}</li>,
    number: ({ children }) => <li>{children}</li>,
  },
};
