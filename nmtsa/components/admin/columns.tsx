import { ColumnDef } from "@tanstack/react-table";

export type Video = {
    title: string;
    transcript: string;
    category: string;
    tags: Array<string>;
    date: string;
    file: string;
    access: string;
};

export const columns: Array<ColumnDef<Video>> = [
    {
        header: "Title",
        accessorKey: "title",
    },
    {
        header: "Transcript",
        accessorKey: "transcript",
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

