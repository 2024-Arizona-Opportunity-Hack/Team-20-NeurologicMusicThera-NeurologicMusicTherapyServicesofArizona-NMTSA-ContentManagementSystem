import { ColumnDef } from "@tanstack/react-table";

export type Article = {
    title: string;
    category: string;
    tags: string;
    date: string;
    path: string;
    thumbnail: string;
    id: string;
    access_groups: Array<string>;
};

export const article_collumns: Array<ColumnDef<Article>> = [
    {
        header: "Title",
        accessorKey: "title",
    },
    {
        header: "Category",
        accessorKey: "category",
    },
    {
        header: "tags",
        accessorKey: "tags",
    },
    {
        header: "Date",
        accessorKey: "date",
    },
    {
        header: "Path",
        accessorKey: "path",
    },
    {
        header: "File",
        accessorKey: "file",
    },
    {
        header: "Access Groups",
        accessorKey: "access_groups",
    },
];

