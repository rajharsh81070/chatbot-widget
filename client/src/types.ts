export interface Message {
  id: number;
  session_id: string;
  content: string;
  is_from_user: boolean;
  created_at: string;
  updated_at: string;
}
