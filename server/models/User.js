import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String },
  role: { type: String, default: 'student', enum: ['student', 'admin', 'evaluator'] },
  createdAt: { type: Date, default: Date.now }
});

export default mongoose.model('User', UserSchema);
