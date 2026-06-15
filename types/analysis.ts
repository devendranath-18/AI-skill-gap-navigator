export interface Resource {
  source: string;
  similarity: number;

  resource: {
    skill: string;
    roadmap: string;
    youtube: string;
    documentation: string;
    projects: string[];
  };
}

export interface AnalysisResult {
  match_score: number;

  resume_skills: string[];

  job_skills: string[];

  matched_skills: string[];

  missing_skills: string[];

  resources: Record<
    string,
    Resource
  >;
}