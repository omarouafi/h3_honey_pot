"use client";
import { useState } from "react";

export default function Home() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
    honeypot: "",
  });

  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    setError(null);
    setSuccess(null);
    e.preventDefault();
    if (formData.honeypot) {
      setError("Bot detected!");
      return;
    }
    setSuccess("Form submitted successfully!");
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100 px-4 sm:px-6 lg:px-8">
      <div className="w-full max-w-md bg-white shadow-lg rounded-2xl p-6 sm:p-8">
        <h2 className="text-2xl font-bold text-center text-gray-900">Contact Us</h2>
        { error && <div className="text-red-500 text-sm mt-4">{error}</div> }
        { success && <div className="text-green-500 text-sm mt-4">{success}</div> }
        <form onSubmit={handleSubmit} className="mt-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Name</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="w-full p-3 mt-1 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="w-full p-3 mt-1 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Message</label>
            <textarea
              name="message"
              value={formData.message}
              onChange={handleChange}
              required
              className="w-full p-3 mt-1 border border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 h-28"
            />
          </div>
          {/* Honeypot field */}
          <div style={{ opacity: 0, position: "absolute", top: 0, left: 0 }}>
            <label>
              Do not fill this field:
              <input type="text" name="honeypot" value={formData.honeypot} onChange={handleChange} />
            </label>
          </div>
          <button
            type="submit"
            className="w-full py-3 text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition duration-200 shadow-md"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  );
}
