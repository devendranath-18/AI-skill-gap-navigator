export const buildPrompt = (
  resume: string,
  jobDescription: string
) => `
You are a senior technical recruiter.

Analyze the resume against the job description.
Return ONLY raw JSON.

Do NOT use markdown.
Do NOT wrap the response in json.
Do NOT include explanations.

{
  "matchScore": number,
  "skills": [],
  "missingSkills": [],
  "strengths": [],
  "suggestions": [],
  "roadmap": []
}

Resume:
${resume}

Job Description:
${jobDescription}
`;