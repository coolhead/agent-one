import { useState } from "react";
import { ask } from "./lib/api";

export default function App() {
  const [q, setQ] = useState("");
  const [a, setA] = useState("");

  return (
    <main className="p-6 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Agent ONE</h1>
      <textarea
        className="w-full border rounded-md p-3 my-3"
        rows={5}
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder="Ask your AI agent something..."
      />
      <button
        className="border bg-blue-600 text-white rounded-md px-4 py-2"
        onClick={async () => setA((await ask(q)).answer)}
      >
        Ask
      </button>
      <pre className="whitespace-pre-wrap mt-4 bg-gray-100 p-3 rounded-md">{a}</pre>
    </main>
  );
}
