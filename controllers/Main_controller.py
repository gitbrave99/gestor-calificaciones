

from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from views.MainView import Ui_MainWindow
from dao.Congrado import ConGrado
from dao.ConMateria import ConMateria
from model.Grado import Grado
from dao.ConEstudiante import ConEstudiante
from dao.ConNotas import ConNotas
from dao.ConExcel import MetodosExcel


class MainViewc(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.cong = ConGrado()
        self.conm = ConMateria()
        self.conest = ConEstudiante()
        self.connot = ConNotas()
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# CARGAS POR DEFECTO
        self.cargar_grados(self.cong.listar_grados())
        # self.cargar_grados_materias(self.cong.listar_grados())
        # carga por defecto de notas
        # self.cargar_calificaciones(self.connot.listar_calificaciones_segun_periodo('I'))

        self.llenarCbxRegistroEstudiante(self.cong.listar_grados_combobox())
        # self.llenarCbxRegistroMaterias(self.conm.listar_materia())
        # BOTON BORRAR BASE DE DTOS
        self.btnBorrarDb.clicked.connect(self.borrarBaseDatos)
        # cargar estudiantes de gardos por defecto
        self.cargarEstudiantesDGradosDefault()

# GENERAR EXCEL
        self.btnExportExcel.clicked.connect(self.generarExcel)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
    # CONECION DE BOTONES DE REGISTRO DE MATERIAS
        self.tblListGradosRegMateria.selectionModel().selectionChanged.connect(
            self.mostrar_materias_segun_grado)
        self.btnAgregarMateria.clicked.connect(self.agregarMateria)
        self.btnActualizarMateria.clicked.connect(self.actualizarMateria)
        self.btnMateriaEdit.clicked.connect(self.selectMateriaAEditar)
        self.btnCancelMateriaEdit.clicked.connect(self.cancelarEditarMateria)
        self.btnEliminarMateria.clicked.connect(self.eliminarMateria)
        self.btnRefreshMaterias.clicked.connect(self.regarcarMaterias)
        

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
    # CONEcCION DE BOTONES  DE REGISTRO DEGRADOS
        self.tblListGrados.selectionModel().selectionChanged.connect(
            self.mostrar_estudiantes_segun_grado)
            
        self.btnAgregarGrado.clicked.connect(self.agregar_grado)
        self.btnGradoEdit.clicked.connect(self.selectGradoAEditar)
        
        self.txtSearchGrado.textChanged.connect(self.buscarGrado)
        self.btnGradoEliminar.clicked.connect(self.eliminarGrado)
        self.btnActualizarGrado.clicked.connect(self.actualizarGrado)
        self.btnCancelGrado.clicked.connect(self.cancelarEditarGrado)
        self.btnRefreshGrados.clicked.connect(self.regarcarGrados)
        self.txtBuscarEstudsRegGrados.textChanged.connect(
            self.buscarEstudiante)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# CONEcCION DE BOTONES  DE REGISTRO ESTUDIANTES
        self.btnCancelEstud.clicked.connect(self.cancelarEditarEstudiante)
        self.btnAgregarEstud.clicked.connect(self.agregarEstudiante)
        self.cbxVerEstudiantesDeRegEst.currentTextChanged.connect(
            self.verEstudianteDeGradosCalificando) 
        
        self.txtBuscarEstuds.textChanged.connect(
            self.buscarEstudianteEnRegistroPorGrado)
        self.btnRefreshEstudiantes.clicked.connect(self.regarcarEstudiantes)
        self.btnEliminarEstud.clicked.connect(self.eliminarEstudiante)
        self.btnCancelEstud.clicked.connect(self.cancelarEditarEstudiante)
        self.btnEditSelectEstud.clicked.connect(self.selectEstudianteEdit)
        self.btnActualizarEstud.clicked.connect(self.actualizarEstudiante)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# CONEcCION DE BOTONES  DE REGISTRO DE NOTAS CALIFIACIONES
        self.txtBuscarRegistroNota.textChanged.connect(self.buscarEstudianteCalicando)
        self.cbxCalifGrados.currentTextChanged.connect(
            self.verEstudiantesACalificarPorGrado)
        self.cbxVerNotasPeriodo.currentTextChanged.connect(
            self.verEstudiantesACalificarPorGradoPeriodo)
        self.cbxVerMateriaPeriodo.currentTextChanged.connect(self.verEstudiantesACalificarPorGradoPeriodoMateria)
        self.btnAgregarNota.clicked.connect(self.agregarCalificacion)
        self.btnEliminarRegistroNota.clicked.connect(self.eliminarNota)
        self.btnRefreshRegistroNotas.clicked.connect(self.refreshRegistroNotas)
        self.btnEditarCalifSelectEstudiante.clicked.connect(self.selectNotaEstudianteEditar)
        self.btnCancelEditNota.clicked.connect(self.cancelarEditarNota)
        self.btnActualizarNota.clicked.connect(self.actualizarCalificacion)
        self.tblListRegistroNotas.selectionModel().selectionChanged.connect(self.mostrar_estudiantes_calificar)


#BORRAR DATOS
    def borrarBaseDatos(self):
        from controllers.ConfirmDelete_controller import ConfirmDeletec
        window = ConfirmDeletec(self)
        window.show()
        window.lblTablaaEliminar.setText('borrarall')
#BORRAR EXCEL
    def generarExcel(self):
        # file_path = QFileDialog.getExistingDirectory()
        #obtener ruta para guardar excel y el nombre
        # file_path= QFileDialog.getSaveFileName()[0]
        file_path= QFileDialog.getSaveFileName(self,'Guardar como','')
        print(f'path= {file_path[0]}')
        ex= MetodosExcel()
        ex.crearBook()
        ex.hojaDefault()
        # ex.crearPlantillaNotas()

        gradosec = str(self.cbxCalifGrados.currentText())
        grado = gradosec[0:-2].strip()
        seccion = gradosec[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = str(pidG[1:-2])
        profesor=self.txtCalifProfesor.text()
        asignatura=str(self.cbxVerMateriaPeriodo.currentText())
        periodo = str(self.cbxVerNotasPeriodo.currentText())
        mat = str(self.cbxVerMateriaPeriodo.currentText())
        if pidG is not None:
            pidG = int(pidG)
            list = self.connot.listar_calificaciones_segun_idGrado_periodo_materia(
                pidG, periodo, mat)
        
        ex.crearPlantillaNotasExcel(list,grado,profesor,asignatura,periodo)
        pathname=file_path[0]+".xlsx"
        ex.guardarArchivo(pathname)

# ***************************************************************************
    # ACTUALIZAR CALIFICCION
    def mostrar_estudiantes_calificar(self):
        tbNota = (self.tblListRegistroNotas.selectionModel().currentIndex())
        estCalf = str(tbNota.sibling(tbNota.row(), 2).data())
        self.txtCalifEstudiante.setText(estCalf)
        

    def actualizarCalificacion(self):
        nota1 = float(self.cbxActI.value())
        nota2 = float(self.cbxActII.value())
        nota3 = float(self.cbxActIII.value())
        idCaf= int(self.txtidCalificacion.text())
        index = (self.tblListRegistroNotas.selectionModel().currentIndex())
        idCalificacion = int(str(index.sibling(index.row(), 0).data()))
        if idCalificacion is not None:
            calificacion = (nota1, nota2, nota3)
            print(calificacion)
            if self.connot.actualizar_notaTercerCiclo(calificacion,idCaf):
                self.refreshRegistroNotas()
                print("CALIFICAION agregada")
                self.cbxActI.setValue(0)
                self.cbxActII.setValue(0)
                self.cbxActIII.setValue(0)
                self.cancelarEditarNota()

    # CANCELAR EDITAR NOTA ESTUDIANTE
    def cancelarEditarNota(self):
        self.btnActualizarNota.setEnabled(False)
        self.btnCancelEditNota.setEnabled(False)
        self.btnAgregarNota.setEnabled(True)
    # SELECIONAR ESTUDIANTE NOTA A EDITAR
    def selectNotaEstudianteEditar(self):
        index = (self.tblListRegistroNotas.selectionModel().currentIndex())
        idCalificacion = index.sibling(index.row(), 0).data()
        if idCalificacion is not None:
            print(type(idCalificacion))
            act1 = str(index.sibling(index.row(), 3).data())
            act2 = str(index.sibling(index.row(), 5).data())
            act3 = str(index.sibling(index.row(), 7).data())
            self.cbxActI.setValue(float(act1))
            self.cbxActII.setValue(float(act2))
            self.cbxActIII.setValue(float(act3))
            self.txtidCalificacion.setText(idCalificacion)
            nperiodo= self.cbxVerNotasPeriodo.currentIndex()
            self.cbxCalifPeriodo.setCurrentIndex(nperiodo)
            materia = self.cbxVerMateriaPeriodo.currentIndex()
            self.cbxCalifMateria.setCurrentIndex(materia)

            self.btnActualizarNota.setEnabled(True)
            self.btnCancelEditNota.setEnabled(True)
            self.btnAgregarNota.setEnabled(False)
    #ELIMINAR NOTA
    def eliminarNota(self):
        from controllers.ConfirmDelete_controller import ConfirmDeletec
        index = (self.tblListRegistroNotas.selectionModel().currentIndex())
        idNota = index.sibling(index.row(), 0).data()
        if idNota is not None:
            window = ConfirmDeletec(self)
            window.show()
            window.lblIdRegAeliminar.setText(str(idNota))
            window.lblTablaaEliminar.setText('nota')
            self.refreshRegistroNotas()
        
    def refreshRegistroNotas(self):
        gradosec = str(self.cbxCalifGrados.currentText())
        grado = gradosec[0:-2].strip()
        seccion = gradosec[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = str(pidG[1:-2])
        if pidG is not None:
            if pidG !='o':
                mat = str(self.cbxVerMateriaPeriodo.currentText())
                pidG = int(pidG)
                list = self.connot.listar_calificaciones_segun_idGrado_periodo_materia(
                    pidG, 'I', mat)
                print(list)
                self.cargar_calificaciones(list)

    # OPERACION DE NOTAS CALIFICACIONES
    def buscarEstudianteCalicando(self,estudiante):
        gradosec = str(self.cbxCalifGrados.currentText())
        grado = gradosec[0:-2].strip()
        seccion = gradosec[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = str(pidG[1:-2])
        if pidG is not None:
            if pidG !='o':
                print(pidG)

                pidG = int(pidG)
                # OBTENEMOS PERIODO
                periodo = str(self.cbxVerNotasPeriodo.currentText())
                materia = str(self.cbxVerMateriaPeriodo.currentText())

                tbOrder=self.connot.buscar_estudiante_calificando(pidG,periodo,materia,estudiante)

                self.cargar_calificaciones(tbOrder)

    def agregarCalificacion(self):
        # mat = str(self.cbxCalifMateria.currentText())
        # matcal = self.conm.buscar_materiaGetId(mat)
        # idMateria = int(matcal[1:-2])
        # periodocal = str(self.cbxCalifPeriodo.currentText())
        nota1 = float(self.cbxActI.value())
        nota2 = float(self.cbxActII.value())
        nota3 = float(self.cbxActIII.value())
        index = (self.tblListRegistroNotas.selectionModel().currentIndex())
        idCalificacion = int(str(index.sibling(index.row(), 0).data()))
        if idCalificacion is not None:
            calificacion = (nota1, nota2, nota3)
            print(calificacion)
            if self.connot.actualizar_notaTercerCiclo(calificacion,idCalificacion):
                self.refreshRegistroNotas()
                print("CALIFICAION agregada")
                self.cbxActI.setValue(0)
                self.cbxActII.setValue(0)
                self.cbxActIII.setValue(0)

    def verEstudiantesACalificarPorGradoPeriodoMateria(self, materia):
        # OBTENEMOS ID GRADO
        if materia !="":
            gradosec = str(self.cbxCalifGrados.currentText())
            grado = gradosec[0:-2].strip()
            seccion = gradosec[-1:]
            pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
            pidG = str(pidG[1:-2])
            periodo = str(self.cbxVerNotasPeriodo.currentText())
            if pidG and periodo is not None:
                print(f'pidg= {pidG}')
                pidG = int(pidG)
                list = self.connot.listar_calificaciones_segun_idGrado_periodo_materia(
                    pidG, periodo, materia)
                self.cargar_calificaciones(list)

    def verEstudiantesACalificarPorGradoPeriodo(self, periodo):
        # OBTENEMOS ID GRADO
        gradosec = str(self.cbxCalifGrados.currentText())
        grado = gradosec[0:-2].strip()
        seccion = gradosec[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = str(pidG[1:-2])
        if pidG is not None:
            pidG = int(pidG)
            mat = str(self.cbxVerMateriaPeriodo.currentText())
            list = self.connot.listar_calificaciones_segun_idGrado_periodo_materia(
                pidG, periodo, mat)
            self.cargar_calificaciones(list)

    def cargar_calificaciones(self, ligrados):
        self.tblListRegistroNotas.setRowCount(len(ligrados))

        for (index_row, row) in enumerate(ligrados):
            for (index_cell, cell) in enumerate(row):
                self.tblListRegistroNotas.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

    def verEstudiantesACalificarPorGrado(self, gradosec):
        grado = gradosec[0:-2].strip()
        seccion = gradosec[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = str(pidG[1:-2])
        if pidG is not None:
            if pidG !='o':
                pidG = int(pidG)
                mat = str(self.cbxVerMateriaPeriodo.currentText())

                print(type(mat))
                print(f"materia={mat}")
                list = self.connot.listar_calificaciones_segun_idGrado_periodo_materia(
                    pidG, 'I', mat)
                print(list)
                self.cargar_calificaciones(list)
                cicle=1
                if  grado.lower() =="bachillerato":
                    cicle=2
                if grado.lower() =="preparatoria":
                    cicle=0
                
                self.llenarCbxRegistroMaterias(self.conm.listar_materia_segun_ciclo(cicle))


# ***************************************************************************
    # OPERACION DE ESTUDIANTES

    def cargarEstudiantesDGradosDefault(self):
        gradosec=str(self.cbxVerEstudiantesDeRegEst.currentText())
        grado = gradosec[0:-2].strip()
        seccion = gradosec[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = pidG[1:-2]
            
        if pidG is not None:
            if pidG!='o':
                list = self.conest.listar_estudiantes_segun_grado(pidG)
                self.cargar_Estudiantes_segun_grado_calificando(list)


    def actualizarEstudiante(self):
        nombre = self.txtRegNomEstud.text()
        if nombre.strip()!="":
            nie = self.txtRegNieEstud.text()
            txtC = str(self.cbxRegGradoEstud.currentText())
            grado = txtC[0:-2].strip()
            seccion = txtC[-1:]
            pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
            pidG = pidG[1:-2]
            print(f'id = {pidG}')
            idEstudiante = self.lblEstudianteToEdit.text()
            student = (nombre, nie, pidG)
            if self.conest.actualizar_estudiante(student, idEstudiante):
                self.txtRegNomEstud.setText("")
                self.txtRegNieEstud.setText("")
                self.regarcarEstudiantes()
                self.limpiarTextosEstudiantes()
                self.btnActualizarGrado.setEnabled(False)
                self.btnCancelGrado.setEnabled(False)
                self.btnAgregarGrado.setEnabled(True)

    def selectEstudianteEdit(self):
        index = (self.tblListEstud.selectionModel().currentIndex())
        idEstudiante = index.sibling(index.row(), 0).data()
        estudiante = index.sibling(index.row(), 1).data()
        nie = index.sibling(index.row(), 2).data()
        self.txtRegNomEstud.setText(estudiante)
        self.txtRegNieEstud.setText(nie)
        self.cbxRegSeccion.setCurrentIndex(1)
        self.lblEstudianteToEdit.setText(idEstudiante)
        txtC = str(self.cbxVerEstudiantesDeRegEst.currentText())

        selItemEdit = self.cbxRegGradoEstud.findText(txtC)
        self.cbxRegGradoEstud.setCurrentIndex(selItemEdit)
        self.btnActualizarEstud.setEnabled(True)
        self.btnCancelEstud.setEnabled(True)
        self.btnAgregarEstud.setEnabled(False)

    def cancelarEditarGrado(self):
        self.btnActualizarEstud.setEnabled(False)
        self.btnCancelEstud.setEnabled(False)
        self.btnAgregarEstud.setEnabled(True)

    def eliminarEstudiante(self):
        from controllers.ConfirmDelete_controller import ConfirmDeletec
        index = (self.tblListEstud.selectionModel().currentIndex())
        idEstudiante = index.sibling(index.row(), 0).data()
        if idEstudiante is not None:
            window = ConfirmDeletec(self)
            window.show()
            window.lblIdRegAeliminar.setText(str(idEstudiante))
            window.lblTablaaEliminar.setText('estudiante')
            # self.llenarCbxGrados(self.cong.listar_grados_combobox())
            # self.llenarCbxRegistroEstudiante(self.cong.listar_grados_combobox())
            self.regarcarEstudiantes()

    def regarcarEstudiantes(self):
        txtC = str(self.cbxVerEstudiantesDeRegEst.currentText())
        grado = txtC[0:-2].strip()
        seccion = txtC[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = pidG[1:-2]
        if pidG is not None:
            if pidG !='o':
                pidG = int(pidG)
                listnm = self.conest.listar_estudiantes_nombre_asc_byIdGrado(pidG)
                self.cargar_Estudiantes_segun_grado_calificando(listnm)

   

    def buscarEstudianteEnRegistroPorGrado(self, text):
        cbx = str(self.cbxVerEstudiantesDeRegEst.currentText())
        grado = cbx[0:-2].strip()
        seccion = cbx[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = str(pidG[1:-2])
        if pidG is not None:
            if pidG !='o':
                pidG = int(pidG)
                print(f'lis {pidG}')
                tblOrder = self.conest.buscarEstudiante(text, pidG)
                self.cargar_Estudiantes_segun_grado_calificando(tblOrder)

    def verEstudianteDeGradosCalificando(self, gradosec):
        grado = gradosec[0:-2].strip()
        seccion = gradosec[-1:]
        pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
        pidG = pidG[1:-2]
            
        if pidG is not None:
            if pidG!='o':
                list = self.conest.listar_estudiantes_segun_grado(pidG)
                self.cargar_Estudiantes_segun_grado_calificando(list)

    def agregarEstudiante(self):
        # VALIDACION
        nombre = self.txtRegNomEstud.text()
        if nombre.strip() !="":
            nie = self.txtRegNieEstud.text()
            txtC = str(self.cbxRegGradoEstud.currentText())
            grado = txtC[0:-2].strip()
            seccion = txtC[-1:]
            pidG = self.conm.listarGradoSeccionIdGrado(grado, seccion)
            pidG = pidG[1:-2]
            nMt = (nombre, nie, pidG)
            if self.conest.agregar_estudiante(nMt):
                self.txtRegNomEstud.setText("")
                self.txtRegNieEstud.setText("")
                self.limpiarTextosEstudiantes()
                # consulta apra obtener el ultimo idestudiante
                idEstudiante = self.conest.obtener_ultimo_estudiante_insertado()
                print(f"ultimo est={idEstudiante}")
                idEstudiante = int(idEstudiante[1:-2])
                # obtener listado de materias del grado registrado
                # liMaterias = self.conm.listar_idMaterias_segun_idGrado(pidG)
                ciclo=1
                if grado.lower()=="bachillerato":
                    ciclo=2
                if grado.lower()=="preparatoria":
                    ciclo=0
                liMaterias = self.conm.listar_idMaterias_segun_ciclo(ciclo)
                i = 0
                p = 0
                pertxt = 'I'
                while p < 4:
                    while i < len(liMaterias):
                        item = str(liMaterias[i])
                        idMateria = int(item[1:-2])
                        calificacion_vacia = (
                            0, 0, 0, pertxt, idEstudiante, idMateria)
                        if self.connot.crearDefault_notaTercerCiclo(calificacion_vacia):
                            print("notas added")
                        i = i + 1
                    i = 0
                    pertxt += 'I'
                    p = p+1
                # agregamos la calificaion vacia

    def cancelarEditarEstudiante(self):
        self.btnActualizarEstud.setEnabled(False)
        self.btnCancelEstud.setEnabled(False)
        self.btnAgregarEstud.setEnabled(True)


# ***************************************************************************
    # OPERACIONES DE MATERIAS

    def regarcarMaterias(self):
        self.mostrar_materias_segun_grado()
        

    def mostrar_materias_segun_grado(self):
        index = (self.tblListGradosRegMateria.selectionModel().currentIndex())
        idGrado = index.sibling(index.row(), 0).data()
        if idGrado is not None:
            list = self.conm.listar_materias_segun_idGrado(idGrado)
            self.cargar_tabla_materias_segun_grado(list)

    def agregarMateria(self):
        
        materia = self.txtRegMateria.text()
        if materia.strip() !="":
                ciclo = str(self.cbxRegMatGrado.currentIndex())

                nMt = (materia, ciclo)
                if self.conm.agregar_materia(nMt):
                    print("materia agregada")
                    #clear campo materia
                    self.txtRegMateria.setText("")
            
            # self.cargar_table_materias(self.cong.listar_grados())

    def selectMateriaAEditar(self):
        materia = (self.tblListMaterias.selectionModel().currentIndex())
        ciclo = (self.tblListGradosRegMateria.selectionModel().currentIndex())
    
        idMateria = materia.sibling(materia.row(), 0).data()
        materia = materia.sibling(materia.row(), 1).data()
        idCiclo=ciclo.sibling(ciclo.row(), 0).data()
        if idCiclo is not None:
            idCiclo = int(idCiclo)
            print(idCiclo)
        
            self.txtRegMateria.setText(materia)
            self.lblMateriaToEdit.setText(idMateria)

            self.cbxRegMatGrado.setCurrentIndex(idCiclo)
            self.btnCancelMateriaEdit.setEnabled(True)
            self.btnActualizarMateria.setEnabled(True)
            self.btnAgregarMateria.setEnabled(False)

    def cancelarEditarMateria(self):
        self.btnActualizarMateria.setEnabled(False)
        self.btnCancelMateriaEdit.setEnabled(False)
        self.btnAgregarMateria.setEnabled(True)

    def actualizarMateria(self):
        materia = self.txtRegMateria.text()
        ciclo = str(self.cbxRegMatGrado.currentIndex())
        
        idMateria = self.lblMateriaToEdit.text()
        materia = (materia, ciclo)
        if self.conm.actualizar_materia(materia, idMateria):
            self.txtRegMateria.setText("")
            self.cargar_grados(self.cong.listar_grados())
            
            self.cancelarEditarMateria()  # inac/activacion de botones

    def eliminarMateria(self):
        from controllers.ConfirmDelete_controller import ConfirmDeletec
        index = (self.tblListMaterias.selectionModel().currentIndex())
        idMateria = index.sibling(index.row(), 0).data()
        if idMateria is not None:
            window = ConfirmDeletec(self)
            window.show()
            window.lblIdRegAeliminar.setText(str(idMateria))
            window.lblTablaaEliminar.setText('materia')
        


# ***************************************************************************
    # OPERACIONES DE GRADO


    def mostrar_estudiantes_segun_grado(self):
        # for ix in selected.indexes():
        self.tblListEstudRegGrados.setRowCount(0)
        #     print("row: {0} col: {1}".format(ix.row(), ix.column()))
        index = (self.tblListGrados.selectionModel().currentIndex())
        idGrado = str(index.sibling(index.row(), 0).data())
        print(idGrado)
        if idGrado is not None:
            idGrado=int(idGrado)
            list = self.conest.listar_estudiantes_segun_grado(idGrado)
            self.cargar_Estudiantes_segun_grado(list)

    def buscarEstudiante(self, text):
        index = (self.tblListGrados.selectionModel().currentIndex())
        idGrado = index.sibling(index.row(), 0).data()
        
        if idGrado is not None:
            tblOrder = self.conest.buscarEstudiante(text, idGrado)
            self.cargar_Estudiantes_segun_grado(tblOrder)

    def regarcarGrados(self):
        self.cargar_grados(self.cong.listar_grados())
        # self.llenarCbxGrados(self.cong.listar_grados_combobox())
        self.tblListEstudRegGrados.setRowCount(0)
        self.recargarAllCbxGrados()
        # self.llenarCbxRegistroEstudiante(self.cong.listar_grados_combobox())

    def cancelarEditarGrado(self):
        self.btnActualizarGrado.setEnabled(False)
        self.btnCancelGrado.setEnabled(False)
        self.btnAgregarGrado.setEnabled(True)

    def actualizarGrado(self):
        ng = Grado()
        ng.grado = self.txtRegGrado.text()
        if ng.grado.strip()!="":
            ng.seccion = self.cbxRegSeccion.currentText()
            idGrado = self.lblIdGradoEdit.text()
            grado = (ng.grado, ng.seccion)
            if self.cong.actualizar_grado(grado, idGrado):
                self.cargar_grados(self.cong.listar_grados())
                self.txtRegGrado.setText("")
                # inac/activacion de botones
                self.btnActualizarGrado.setEnabled(False)
                self.btnCancelGrado.setEnabled(False)
                self.btnAgregarGrado.setEnabled(True)

    def agregar_grado(self):
        ng = Grado()
        ng.grado = self.txtRegGrado.text()
        if ng.grado.strip()!="":
            ng.seccion = self.cbxRegSeccion.currentText()
            grado = (ng.grado, ng.seccion)
            if self.cong.agregar_grado(grado):
                # Cargar tabla
                self.cargar_grados(self.cong.listar_grados())
                self.recargarAllCbxGrados()
                self.txtRegGrado.setText("")
                # self.llenarCbxGrados(self.cong.listar_grados_combobox())
                # self.llenarCbxRegistroEstudiante(
                #     self.cong.listar_grados_combobox())

    def recargarAllCbxGrados(self):
        ligrados=self.cong.listar_grados_combobox()
        
        self.cbxVerEstudiantesDeRegEst.clear()
        self.cbxRegGradoEstud.clear()
        self.cbxCalifGrados.clear()
        i = 0
        while i < len(ligrados):
            item = str(ligrados[i])
            
            self.cbxRegGradoEstud.addItem(item[2:-3])
            self.cbxVerEstudiantesDeRegEst.addItem(item[2:-3])
            self.cbxCalifGrados.addItem(item[2:-3])
            i = i + 1

    def buscarGrado(self, text):
        tblOrder = self.cong.buscarGrado(text)
        self.cargar_grados(tblOrder)

    def buscarGradoMateria(self, text):
        tblOrder = self.cong.buscarGrado(text)
        self.cargar_grados_materias(tblOrder)

    def selectGradoAEditar(self):
        # print("slected: ", self.tblListGrados.currentRow()+1)
        # print("values: ",self.tblListGrados.cellWidget(0,1))
        index = (self.tblListGrados.selectionModel().currentIndex())
        idGrado = index.sibling(index.row(), 0).data()
        if idGrado is not None:
            grado = index.sibling(index.row(), 1).data()
            seccion = index.sibling(index.row(), 2).data()
            self.txtRegGrado.setText(grado)
            self.cbxRegSeccion.setCurrentIndex(1)
            self.lblIdGradoEdit.setText(idGrado)
            selItemEdit = self.cbxRegSeccion.findText(seccion)
            self.cbxRegSeccion.setCurrentIndex(selItemEdit)
            self.btnActualizarGrado.setEnabled(True)
            self.btnCancelGrado.setEnabled(True)
            self.btnAgregarGrado.setEnabled(False)

        # print("find: ", self.cbxRegSeccion.findText(seccion))

    def eliminarGrado(self):
        from controllers.ConfirmDelete_controller import ConfirmDeletec
        index = (self.tblListGrados.selectionModel().currentIndex())
        idGrado = index.sibling(index.row(), 0).data()
        
        if idGrado is not None:
            window = ConfirmDeletec(self)
            window.show()

            window.lblIdRegAeliminar.setText(str(idGrado))
            window.lblTablaaEliminar.setText('grado')
            # self.llenarCbxGrados(self.cong.listar_grados_combobox())
            self.tblListEstudRegGrados.setRowCount(0)
            # self.llenarCbxRegistroEstudiante(self.cong.listar_grados_combobox())

    


# ***************************************************************************
# METODOS NECESARIOS DE VISTA


    def cargar_grados(self, ligrados):
        self.tblListGrados.setRowCount(len(ligrados))
        
        for (index_row, row) in enumerate(ligrados):
            for (index_cell, cell) in enumerate(row):
                self.tblListGrados.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))
                

    def cargar_grados_registro_estudiante(self, ligrados):
        self.tblListGradosRegMateria.setRowCount(len(ligrados))

        for (index_row, row) in enumerate(ligrados):
            for (index_cell, cell) in enumerate(row):
                self.tblListGradosRegMateria.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

    def cargar_grados_materias(self, ligrados):
        self.tblListGradosRegMateria.setRowCount(len(ligrados))

        for (index_row, row) in enumerate(ligrados):
            for (index_cell, cell) in enumerate(row):
                self.tblListGradosRegMateria.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

  

    def llenarCbxRegistroMaterias(self, list):
        self.cbxCalifMateria.clear()
        self.cbxVerMateriaPeriodo.clear()
        i = 0
        while i < len(list):
            item = str(list[i])
            self.cbxCalifMateria.addItem(item[2:-3])
            self.cbxVerMateriaPeriodo.addItem(item[2:-3])
            i = i + 1

    def llenarCbxRegistroEstudiante(self, ligrados):
        self.cbxVerEstudiantesDeRegEst.clear()
        self.cbxRegGradoEstud.clear()
        self.cbxCalifGrados.clear()
        i = 0
        while i < len(ligrados):
            item = str(ligrados[i])
            self.cbxVerEstudiantesDeRegEst.addItem(item[2:-3])
            self.cbxRegGradoEstud.addItem(item[2:-3])
            self.cbxCalifGrados.addItem(item[2:-3])
            i = i + 1

    def cargar_tabla_materias_segun_grado(self, liMaterias):
        self.tblListMaterias.setRowCount(len(liMaterias))
        for (index_row, row) in enumerate(liMaterias):
            for (index_cell, cell) in enumerate(row):
                self.tblListMaterias.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

    def cargar_Estudiantes_segun_grado(self, liEstuds):
        self.tblListEstudRegGrados.setRowCount(0)
        self.tblListEstudRegGrados.setRowCount(len(liEstuds))

        for (index_row, row) in enumerate(liEstuds):
            for (index_cell, cell) in enumerate(row):
                self.tblListEstudRegGrados.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

    def cargar_table_materias(self, listMaterias):
        self.tblListMaterias.setRowCount(len(listMaterias))
        for (index_row, row) in enumerate(listMaterias):
            for (index_cell, cell) in enumerate(row):
                self.tblListMaterias.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

        # OPERACIN ESTUDIANTE
    def cargar_Estudiantes_segun_grado_calificando(self, liEstuds):
        self.tblListEstud.setRowCount(0)
        self.tblListEstud.setRowCount(len(liEstuds))

        for (index_row, row) in enumerate(liEstuds):
            for (index_cell, cell) in enumerate(row):
                self.tblListEstud.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell)))

    def limpiarTextosEstudiantes(self):
        self.txtRegNomEstud.setText("")
        self.txtRegNieEstud.setText("")
