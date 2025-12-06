import { Link } from "react-router-dom";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const data = [
  { name: "Late Blight", accuracy: 93 },
  { name: "Early Blight", accuracy: 89 },
  { name: "Leaf Mold", accuracy: 76 },
  { name: "Healthy", accuracy: 98 },
];

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center py-10">
      <nav className="w-full bg-white shadow-lg p-4 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-green-700">🍅 Tomato Leaf Dashboard</h1>
        <Link
          to="/upload"
          className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Upload Leaf
        </Link>
      </nav>

      <div className="w-full max-w-4xl mt-10 bg-white p-8 rounded-2xl shadow-md">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">Detection Accuracy Overview</h2>
        <BarChart width={600} height={300} data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="accuracy" fill="#22c55e" />
        </BarChart>
      </div>
    </div>
  );
}
