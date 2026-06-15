import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
interface LearningResource {
  skill?: string;
  roadmap?: string;
  youtube?: string;
  documentation?: string;
  projects?: string[];
}

interface ResourceItem {
  resource?: LearningResource;
  similarity?: number;
  source?: string;
  message?: string;
}

interface Result {
  matchScore: number;
  skills: string[];
  missingSkills: string[];
  resources?: Record<string, ResourceItem>;
}

interface Props {
  result: Result;
}

export default function ResultCard({
  result,
}: Props) {
   console.log("RESULT:", result);
  console.log("RESOURCES:", result.resources);
  return (
    <div className="bg-white rounded-[32px] border border-slate-200 shadow-2xl p-10">
      {/* Header */}
      <div className="flex gap-3 mb-8">
        <div className="w-4 h-4 rounded-full bg-green-500" />
        <div className="w-4 h-4 rounded-full bg-yellow-500" />
        <div className="w-4 h-4 rounded-full bg-red-500" />
      </div>

      {/* Resume Score */}
      <div className="bg-slate-50 rounded-3xl p-8 mb-8">
        <h2 className="font-bold text-2xl mb-5">
          Resume Score
        </h2>

        <div className="w-full bg-slate-200 rounded-full h-5 overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-emerald-400 to-green-600"
            style={{
              width: `${result.matchScore}%`,
            }}
          />
        </div>

        <p className="mt-4 text-xl font-bold text-emerald-600">
          {result.matchScore}% Match
        </p>
      </div>

      {/* Skills Found */}
      <div className="bg-slate-50 rounded-3xl p-8 mb-8">
        <h3 className="font-bold text-xl mb-5">
          Skills Found
        </h3>

        <div className="flex flex-wrap gap-3">
          {result.skills?.map((skill) => (
            <span
              key={skill}
              className="px-4 py-2 rounded-full bg-green-100 text-green-700 font-medium"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* Missing Skills */}
      <div className="bg-slate-50 rounded-3xl p-8 mb-8">
        <h3 className="font-bold text-xl mb-5">
          Missing Skills
        </h3>

        <div className="flex flex-wrap gap-3">
          {result.missingSkills?.map((skill) => (
            <span
              key={skill}
              className="px-4 py-2 rounded-full bg-red-100 text-red-600 font-medium"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* Learning Resources */}
     {/* Learning Resources */}
<div className="bg-slate-50 rounded-3xl p-8">
  <h3 className="font-bold text-2xl mb-6">
    Learning Resources
  </h3>

  <Accordion
    type="single"
    collapsible
    className="w-full"
  >
    {Object.entries(
      result.resources || {}
    ).map(([skill, value]) => {
      const resource = value.resource;

      if (!resource) {
        return (
          <div
            key={skill}
            className="bg-yellow-50 border border-yellow-200 rounded-2xl p-5 mb-4"
          >
            <h4 className="font-semibold text-lg">
               {skill.toUpperCase()}
            </h4>

            <p className="text-yellow-700 mt-2">
              {value.message ||
                "No learning resources found"}
            </p>
          </div>
        );
      }

      return (
        <AccordionItem
          key={skill}
          value={skill}
          className="bg-white rounded-2xl border px-5 mb-4"
        >
          <AccordionTrigger className="font-semibold text-lg hover:no-underline">
            🚀 {skill.toUpperCase()}
          </AccordionTrigger>

          <AccordionContent>
            <div className="space-y-4 pt-2">
              {resource.roadmap && (
                <a
                  href={resource.roadmap}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block p-4 rounded-xl bg-emerald-50 hover:bg-emerald-100 transition"
                >
                  🗺️ Roadmap
                </a>
              )}

              {resource.youtube && (
                <a
                  href={resource.youtube}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block p-4 rounded-xl bg-red-50 hover:bg-red-100 transition"
                >
                  ▶️ YouTube Course
                </a>
              )}

              {resource.documentation && (
                <a
                  href={resource.documentation}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block p-4 rounded-xl bg-blue-50 hover:bg-blue-100 transition"
                >
                  📚 Documentation
                </a>
              )}

              {resource.projects &&
                resource.projects.length > 0 && (
                  <div className="bg-slate-100 rounded-xl p-4">
                    <h4 className="font-semibold mb-3">
                      💻 Practice Projects
                    </h4>

                    <ul className="space-y-2">
                      {resource.projects.map(
                        (project) => (
                          <li
                            key={project}
                            className="text-slate-700"
                          >
                            • {project}
                          </li>
                        )
                      )}
                    </ul>
                  </div>
                )}

              {value.similarity !==
                undefined && (
                <div className="text-xs text-slate-500 border-t pt-3">
                  Similarity Match:{" "}
                  {value.similarity.toFixed(
                    2
                  )}
                  %
                </div>
              )}
            </div>
          </AccordionContent>
        </AccordionItem>
      );
    })}
  </Accordion>
</div>
    </div>
  );
}