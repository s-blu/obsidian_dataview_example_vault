const inlinksFromUseCases = input?.current?.file.inlinks.filter(link => link.path.contains("33 Use Cases")) ?? [];

const header = `> [!info] Part of Use Cases`;

if (inlinksFromUseCases.length > 1) {
	const list = inlinksFromUseCases.array().reduce((acc, curr) => `${acc}</br> - ${curr}`,"")

	dv.span(`${header}
    > This query is part of following use cases:
    > ${list}
    > 
	`)
} else if (inlinksFromUseCases.length === 1) {
	dv.span(`${header}
    > This query is part of use case ${inlinksFromUseCases[0]}.
	`)
}