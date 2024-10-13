import { ColumnDef } from "@tanstack/react-table";

export type User = {
    first: string;
    last: string;
    email: string;
    groups: Array<string>;
};

export const user_columns: Array<ColumnDef<User>> = [
    {
        header: "First name",
        accessorKey: "first",
    },
    {
        header: "Last name",
        accessorKey: "last",
    },
    {
        header: "Email",
        accessorKey: "email",
    },
    {
        header: "Access Groups",
        accessorKey: "groups",
    },
];