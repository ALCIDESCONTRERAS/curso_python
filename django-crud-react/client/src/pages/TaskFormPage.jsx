import { useForm } from "react-hook-form";
import { createTask, deleteTask, updateTask, getTask } from "../api/tasks.api";
import { useNavigate, useParams } from "react-router-dom";
import { useEffect } from "react";
import { toast } from "react-hot-toast";

export const TaskFormPage = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
    setValue,
  } = useForm();

  const params = useParams();

  const onSubmit = handleSubmit(async (data) => {
    if (params.id) {
      updateTask(params.id, data);
      toast.success("Task updated", {
        position: "bottom-right",
        style: {
          background: "#101010",
          color: "#fff",
        },
      });
    } else {
      await createTask(data);
      toast.success("Task created", {
        position: "bottom-right",
        style: {
          background: "#101010",
          color: "#fff",
        },
      });
    }
    navigate("/");
  });

  const navigate = useNavigate();

  useEffect(() => {
    async function loadTask() {
      if (params.id) {
        const {
          data: { title, Description },
        } = await getTask(params.id);
        setValue("title", title);
        setValue("Description", Description);
      }
    }
    loadTask();
  }, []);

  return (
    <main className="max-w-xl mx-auto">
      <form onSubmit={onSubmit}>
        <input
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
          type="text"
          placeholder="title"
          {...register("title", { required: true })}
        />
        {errors.title && <span>this field is required</span>}

        <textarea
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
          rows="3"
          placeholder="Description"
          {...register("Description", { required: true })}
        ></textarea>

        {errors.description && <span>this field is required</span>}

        <button className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
          Save
        </button>
        <section className="flex justify-end">
          {params.id && (
            <button
              className="bg-red-500 p-3 rounded-lg w-48 mt-3"
              onClick={async () => {
                const accepted = window.confirm("are you sure?");
                if (accepted) {
                  await deleteTask(params.id);
                  toast.success("Task deleted", {
                    position: "bottom-right",
                    style: {
                      background: "#101010",
                      color: "#fff",
                    },
                  });
                  navigate("/");
                }
              }}
            >
              Delete
            </button>
          )}
        </section>
      </form>
    </main>
  );
};
