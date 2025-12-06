import { useState } from "react";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Please select an image");

    const formData = new FormData();
    formData.append("image", file);

    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center items-center space-y-6">
      <h2 className="text-3xl font-bold text-gray-800">Upload Tomato Leaf Image</h2>

      <input
        type="file"
        accept="image/*"
        onChange={(e) => setFile(e.target.files[0])}
        className="border rounded-md p-2"
      />

      <button
        onClick={handleUpload}
        className="bg-green-600 text-white px-6 py-2 rounded-md hover:bg-green-700 transition"
      >
        Upload & Detect
      </button>

      {result && (
        <div className="bg-white shadow-lg rounded-xl p-6 text-center w-80">
          <h3 className="text-lg font-bold text-gray-700 mb-2">Prediction Result</h3>
          <p className="text-blue-600 font-semibold text-xl">{result.predicted_class}</p>
          <p className="text-gray-500 text-sm">
            Confidence: {result.confidence.toFixed(2)}%
          </p>
        </div>
      )}
    </div>
  );
}
