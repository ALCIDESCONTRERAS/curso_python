import { Link } from "react-router-dom";

export const Navigation = () => {
  return (
    <div className="flex justify-between py-3">
      <Link to={"/tasks"}>
        <h1 className="font-bold text-3xl mb-4">Task App</h1>
      </Link>
      <button className="bg-indigo-500 px-3 rounded-lg">
        <Link to={"/tasks-create"}>Create task</Link>
      </button>
    </div>
  );
};
