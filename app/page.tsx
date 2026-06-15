"use client";

import { useState } from "react";
import UploadForm from "@/components/ui/upload-form";
import ResultCard from "@/components/ui/result-card";

const sampleResult = {
  matchScore: 82,

  skills: [
    "React",
    "Node.js",
    "MongoDB",
    "SQL",
    "Python",
    "Git",
  ],

  missingSkills: [
    "AWS",
    "Docker",
    "TypeScript",
  ],

  resources: {
    AWS: {
      resource: {
        roadmap: "https://roadmap.sh/aws",
      },
    },

    Docker: {
      resource: {
        roadmap: "https://roadmap.sh/docker",
      },
    },

    TypeScript: {
      resource: {
        roadmap:
          "https://roadmap.sh/typescript",
      },
    },
  },
};

export default function HomePage() {
  const [result, setResult] =
    useState(sampleResult);

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 via-emerald-50 to-violet-50">
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="grid lg:grid-cols-2 gap-16 items-start">
          <UploadForm setResult={setResult} />

          <ResultCard result={result} />
        </div>
      </div>
    </main>
  );
}