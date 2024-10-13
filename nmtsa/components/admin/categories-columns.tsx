import { ColumnDef } from "@tanstack/react-table";

export type Category = {
    id: string;
    name: string;
};

export const category_collumns: Array<ColumnDef<Category>> = [
    {
        header: "ID",
        accessorKey: "id",
    },
    {
        header: "Name",
        accessorKey: "name",
    },
];

