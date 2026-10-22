import mongoose from 'mongoose';

const AttemptSchema = new mongoose.Schema({
  userId: { type: String, required: true },
  studentName: { type: String, required: true },
  attemptType: { type: String, required: true }, // 'quiz', 'drill', 'coding', 'practice'
  topic: { type: String, required: true }, // 'Python', 'Java', 'DSA', 'DBMS', 'Web Development'
  score: { type: Number, required: true, min: 0, max: 100 },
  feedback: { type: String, default: '' },
  timeTakenSec: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now }
});

export default mongoose.model('Attempt', AttemptSchema);
