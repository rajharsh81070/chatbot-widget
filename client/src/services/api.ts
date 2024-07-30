import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/v1/chat",
  withCredentials: true,
});

export const startSession = async () => {
  const response = await api.post("/start_session");
  return response.data.data.session_id;
};

export const createMessage = async (content: string) => {
  const response = await api.post("/create_message", { content });
  return response.data.data;
};

export const editMessage = async (messageId: number, content: string) => {
  const response = await api.patch(`/edit_message/${messageId}`, { content });
  return response.data.data;
};

export const deleteMessage = async (messageId: number) => {
  await api.delete(`/delete_message/${messageId}`);
};
