import mongoose from 'mongoose';

const CompanySchema = new mongoose.Schema({
  name: { type: String, required: true },
  slug: { type: String, required: true, unique: true },
  logo: { type: String },
  tier: { type: String },
  industry: { type: String },
  eligibility: { type: String },
  skills: [{ type: String }],
  rounds: [{
    roundNum: Number,
    name: String,
    type: String,
    duration: String,
    description: String,
    tips: String
  }],
  sampleQuestions: [{
    topic: String,
    difficulty: String,
    question: String
  }]
});

export default mongoose.model('Company', CompanySchema);
