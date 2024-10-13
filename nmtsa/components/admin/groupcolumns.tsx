import { ColumnDef } from "@tanstack/react-table";

export type Video = {
    id: number,
    group_name: string
};

export const groupcolumns: Array<ColumnDef<Video>> = [
    {
        header: "ID",
        accessorKey: "id",
    },
    {
        header: "Group Name",
        accessorKey: "group_name",
    },
];

