import { Command, Flags } from "@oclif/core";

export default class Hello extends Command {
	static override flags = {
		flag: Flags.boolean(),
	};

	public async run(): Promise<void> {
		const { flags } = await this.parse(Hello);
		this.log("Hello from oclif!");
		this.log("flag: %s", flags.flag ? "yes" : "no");
	}
}