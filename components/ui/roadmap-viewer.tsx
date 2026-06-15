"use client";

import ReactMarkdown from "react-markdown";

interface Props {
  roadmap: string;
}

export default function RoadmapViewer({
  roadmap,
}: Props) {
  return (
    <div className="prose prose-sm max-w-none dark:prose-invert">
      <ReactMarkdown>
        {roadmap}
      </ReactMarkdown>
    </div>
  );
}