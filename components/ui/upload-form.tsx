"use client";

import { useState } from "react";

interface Props {
  setResult: (data: any) => void;
}

export default function UploadForm({
  setResult,
}: Props) {
  const [file, setFile] =
    useState<File | null>(null);

  const [jobDescription, setJobDescription] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  async function handleSubmit() {
    if (!file) return;

    try {
      setLoading(true);

      const formData = new FormData();

      formData.append(
        "file",
        file
      );

      formData.append(
        "job_description",
        jobDescription
      );

      const response = await fetch(
        "http://localhost:8000/analyze-pdf",
        {
          method: "POST",
          body: formData,
        }
      );

      const data =
        await response.json();

      setResult({
        matchScore:
          data.match_score,

        skills:
          data.resume_skills,

        missingSkills:
          data.missing_skills,

        resources:
          data.resources,
      });
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <p className="text-emerald-600 font-bold tracking-widest uppercase mb-4">
        AI Skill gap navigator
      </p>

      <h1 className="text-6xl font-bold text-slate-900 leading-tight mb-6">
        Is your resume
        <br />
        good enough?
      </h1>

      <p className="text-xl text-slate-600 mb-10">
        Upload your resume and compare
        it against a job description.
        Discover missing skills and get
        personalized learning resources.
      </p>

      <div className="bg-white rounded-3xl border p-8 shadow-xl">
        <div className="space-y-6">
          <div>
            <label className="font-semibold">
              Upload Resume PDF
            </label>

            <div className="mt-3 border-2 border-dashed border-emerald-300 rounded-2xl p-6">
              <input
                type="file"
                accept=".pdf"
                onChange={(e) =>
                  setFile(
                    e.target.files?.[0] ??
                      null
                  )
                }
              />

              {file && (
                <p className="mt-3 text-sm text-slate-600">
                  {file.name}
                </p>
              )}
            </div>
          </div>

          <div>
            <label className="font-semibold">
              Job Description
            </label>

            <textarea
              rows={8}
              value={jobDescription}
              onChange={(e) =>
                setJobDescription(
                  e.target.value
                )
              }
              className="w-full mt-3 rounded-xl border p-4"
              placeholder="Paste Job Description..."
            />
          </div>

          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full py-4 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white font-bold transition"
          >
            {loading
              ? "Analyzing..."
              : "Analyze Resume"}
          </button>
        </div>
      </div>
    </div>
  );
}