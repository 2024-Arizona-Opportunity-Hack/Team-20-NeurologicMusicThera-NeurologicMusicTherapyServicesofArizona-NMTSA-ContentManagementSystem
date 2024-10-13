import { ColumnDef } from "@tanstack/react-table";

export type Article = {
    title: string;
    transcript: string;
    category: string;
    tags: Array<string>;
    date: string;
    file: string;
    access: string;
};

export const articlecolumns: Array<ColumnDef<Article>> = [
    {
        header: "Title",
        accessorKey: "title",
    },
    {
        header: "Category",
        accessorKey: "category",
    },
    {
        header: "Tags",
        accessorKey: "tags",
    },
    {
        header: "Date",
        accessorKey: "date",
    },
    {
        header: "File",
        accessorKey: "file",
    },
    {
        header: "Access",
        accessorKey: "access",
    },
];

