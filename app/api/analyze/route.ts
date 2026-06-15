import { NextResponse } from "next/server";

export async function POST(
  request: Request
) {
  try {
    const formData =
      await request.formData();

    const response =
      await fetch(
        "http://127.0.0.1:8000/analyze-pdf",
        {
          method: "POST",
          body: formData,
        }
      );

    if (!response.ok) {
      throw new Error(
        "FastAPI request failed"
      );
    }

    const data =
      await response.json();

    return NextResponse.json(
      data
    );
  } catch (error) {
    console.error(error);

    return NextResponse.json(
      {
        error:
          "Analysis failed",
      },
      {
        status: 500,
      }
    );
  }
}