export const INITIAL_MESSAGE = (id: string) => ({
  id: Math.max(),
  content: "Hi, I'm Ava. How can I help you today?",
  is_from_user: false,
  created_at: new Date().toISOString(),
  session_id: id,
  updated_at: new Date().toISOString(),
});
