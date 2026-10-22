import mongoose from 'mongoose';

const QuestionSchema = new mongoose.Schema({
  topic: { type: String, required: true },
  qType: { type: String, required: true, enum: ['mcq', 'interview', 'code'] },
  difficulty: { type: String, required: true, enum: ['easy', 'medium', 'hard'] },
  title: { type: String, required: true },
  question: { type: String, required: true },
  options: [{ type: String }],
  correctAnswer: { type: String },
  explanation: { type: String },
  hints: [{ type: String }],
  starterCode: { type: String },
  testCases: [{ type: Object }]
});

export default mongoose.model('Question', QuestionSchema);
