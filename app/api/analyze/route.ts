import { NextResponse } from "next/server";

export async function POST(
  request: Request
) {
  try {
    const formData =
      await request.formData();

    const response = await fetch(
  `${process.env.NEXT_PUBLIC_API_URL}/analyze-pdf`,
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