import OpenAI from 'openai';



async function main() {
  
}

class LLM {
    model_name: string;
    client: OpenAI;
    messages: OpenAI.ChatCompletionMessageParam[]

    constructor (model_name: string, system_message: string | undefined) {
        this.model_name = model_name;
        this.client = new OpenAI();

        this.messages = []

        if (system_message) {
            this.messages.push({
                'role': 'system',
                'content': system_message
            })
        }
    }

    async inference (phrase: string) {
        const chatCompletion = await this.client.chat.completions.create({
            messages: ,
            model: 'gpt-4o-mini',
        });
    }
}