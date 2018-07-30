        #include <iostream>
        #include <fstream>
        #include <string>
        #include <sstream>

        using namespace std;
        struct record {
            string name;
            ostringstream data_runs;
            int CN;
            int FBCN;
            int off;
            int NDS;
            int attr30And80;
            

        };
        //send a record signature to indicate a record
        int readRecordSignature(ifstream &file, int offset, int length)
        {
            int dec;
            file.seekg(offset, file.beg);
            char* buffer = new char[length];
            file.read(buffer, length);
            dec = *(reinterpret_cast<int *>(buffer));
            delete [] buffer;
            return dec;
        }
        //read bytes from a file based on offset and length
        char* readBytes(ifstream &file, int offset, int length) 
        {
            file.seekg(offset, file.beg);
            char* buffer = new char[length];
            file.read(buffer, length);
            return buffer;
        }
        //from boot sector 
        int main(int argc, char** argv)
        {

            if (argc != 2) {
                cout << "The number of argument is not equal to two" << endl;
            }
            string name;
            int offset;
            int length;
            int MFTZONE_BYTES;
            ifstream img(argv[1], ifstream::binary);
            //gets bytes per sector
            char* ptr = readBytes(img, 0x0B,2);
            int BYTES_PER_SECTOR = *(reinterpret_cast<int* > (ptr));
            delete ptr;
            //gets sector per cluster
            ptr = readBytes(img, 0x0D,1);
            int SECTORS_PER_CLUSTER = *(ptr);
            delete ptr;
            //calculating from bootsector to mtf zone
            length=8;
            offset=48;
            ptr = readBytes(img, offset, length);
            //gets the MFT zone address
            MFTZONE_BYTES = *(reinterpret_cast<long long*>(ptr)) * BYTES_PER_SECTOR * SECTORS_PER_CLUSTER;
            delete ptr;
            //getting to the first record
            length = 4;
            int i=0;
            int first_Attribute_Offset;
            uint8_t  attributeID;
            int RECORD_ADDRESS = MFTZONE_BYTES;
            int ATTRIBUTE_LENGTH;
            int ATTRIBUTE_ADDRESS;
            record rc = {};
            //looping every record with the record signature
            while(readRecordSignature(img, RECORD_ADDRESS, length) == 0x454C4946) {//while it's record
                ptr = readBytes(img, RECORD_ADDRESS + 0x14, 2);
                first_Attribute_Offset = *(reinterpret_cast<short* >(ptr));
                delete ptr;
                ATTRIBUTE_ADDRESS = RECORD_ADDRESS + first_Attribute_Offset;//first attribute after the header
                ATTRIBUTE_LENGTH = first_Attribute_Offset;
                //looping through every attribute in the record
              while( ATTRIBUTE_LENGTH != 0 && ATTRIBUTE_ADDRESS < (RECORD_ADDRESS + 1024)){
                ptr = readBytes(img, ATTRIBUTE_ADDRESS, 1);	
                attributeID =  *(ptr);
                delete ptr;
                if (attributeID == 0x30 && rc.attr30And80 == 0){
                    rc.attr30And80 +=1;
                    rc.CN= (RECORD_ADDRESS/BYTES_PER_SECTOR)/SECTORS_PER_CLUSTER;//cluster number where MFT record begins
                    ptr = readBytes(img, ATTRIBUTE_ADDRESS + offset, 2);
                    ATTRIBUTE_LENGTH = *(reinterpret_cast<short * >(ptr));
                    delete ptr;
                    length = ATTRIBUTE_LENGTH - 0x5A; //the length of a name
                    ptr = readBytes(img, ATTRIBUTE_ADDRESS + 0x5A, length);
                    if ( ptr != NULL){
                         rc.name.assign(ptr, length);
                    } 
                    delete ptr;
                    rc.FBCN = 0;
                } else if (attributeID == 0x80) {
                    rc.attr30And80 +=1;
                    rc.NDS += 1;
                    offset = 0x08;
                    ptr = readBytes(img, ATTRIBUTE_ADDRESS + offset, 1);
                    int resident = *ptr;
                    delete ptr;
                    if(resident == 0 && rc.attr30And80 == 2){ //if it's resident and data stream
                        rc.FBCN = rc.CN;
                        offset = 0x14;
                        ptr = readBytes(img, ATTRIBUTE_ADDRESS + offset, 2);
                        rc.off = (ATTRIBUTE_ADDRESS + *(reinterpret_cast<short *> (ptr) )) % rc.FBCN;//(rc.FBCN * SECTORS_PER_CLUSTER * BYTES_PER_SECTOR);
                        delete ptr; 
                    } else if(resident == 0x01 && rc.attr30And80 == 2){ //if none resident and not a data stream
                        rc.off = 0;
                        int dataRunOffset = 0x40;
                        uint16_t first4bits;
                        uint16_t last4bits;
                        uint16_t bits;
                        int count;
                        int VCN=0;
                        int LCN=0;
                        unsigned int temp;
                        offset=0;
                        ptr = readBytes(img, ATTRIBUTE_ADDRESS + dataRunOffset,1);
                        bits = *(ptr);
                        delete ptr;
                        while (bits !=0) {

                            first4bits = (bits & 0x00F0) >> 4;
                            last4bits = bits & 0xF;
                            ptr = readBytes(img, (ATTRIBUTE_ADDRESS + dataRunOffset +  offset + 1) , last4bits);//reading  count
                            int i=last4bits;
                            while (i>0) {
                                temp = (reinterpret_cast<unsigned char& > (*(ptr+(i-1))))<<((i-1)*8);
                                count += temp;
                                i--;
                            }
                            delete ptr;
                            ptr = readBytes(img, (ATTRIBUTE_ADDRESS + dataRunOffset + offset + 1 + last4bits), first4bits); //reading LCA
                            i = first4bits;
                            while (i>0){
                                if(i<first4bits)
                                    temp = (reinterpret_cast<unsigned char& > (*(ptr+(i-1))))<<((i-1)*8);
                                else 
                                    temp = (*(ptr+(i-1)))<<((i-1)*8);
                                VCN += temp;//making it little endian
                                i--;
                            }
                            temp =0;
                            delete ptr;
                            if (LCN == 0) {//the first LCN
                                rc.FBCN = VCN;
                            }
                            LCN += VCN;
                            i=0;
                            rc.data_runs << " (" << LCN << "," <<count<<")";
                            count = 0;
                            VCN = 0;
                            offset += first4bits + last4bits + 1;
                            ptr = readBytes(img, ATTRIBUTE_ADDRESS + dataRunOffset + offset, 1);
                            bits = *(ptr);
                            delete ptr;
                        }//closing the data run while loop
                        LCN = 0;
                    }//closing the if none resident condition
                }//cloing the if data attribution condition
                 offset = 0x04;
                 ptr = readBytes(img, ATTRIBUTE_ADDRESS + offset,2);
                 ATTRIBUTE_LENGTH = *(reinterpret_cast<short* >(ptr));
                 delete ptr;
                 ATTRIBUTE_ADDRESS += ATTRIBUTE_LENGTH;
            }//closing while attribute loop
                //printing out the output of a record
            if ( rc.attr30And80 >= 2) {
                cout << endl;
                cout << rc.name << ":" << endl;
                if ((rc.NDS-1) != 0 && rc.data_runs.str() != "") 
                    cout << rc.CN << ":: " << rc.FBCN << "(+" << rc.off << ") :: " << rc.NDS - 1  <<" :: " << rc.data_runs.str()<< "" << endl;
                else if ((rc.NDS-1) == 0 && rc.data_runs.str() != "")
                     cout << rc.CN << ":: " << rc.FBCN << "(+" << rc.off << ") :: " << rc.data_runs.str() << "" << endl;
                else if ((rc.NDS-1) != 0 && rc.data_runs.str() == "" )
                     cout << rc.CN << ":: " << rc.FBCN << "(+" << rc.off << ") :: " << rc.NDS - 1  << ""<< endl;
                else 
                    cout << rc.CN << ":: " << rc.FBCN << "(+" << rc.off << ")" << "" << endl;


                }
            rc.data_runs.str("");
            rc.attr30And80 = 0;
            rc.NDS = 0;
            RECORD_ADDRESS += 1024;
            } //closing while record attribute
            return 0;
        }
