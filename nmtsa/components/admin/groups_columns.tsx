import { ColumnDef } from "@tanstack/react-table";

export type Group = {
    category: string;
    title: string;
    users: Array<string>;
};

export const group_columns: Array<ColumnDef<Group>> = [
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

