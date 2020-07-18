package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.IDifferential;
import www.google.com.digitalbuildings._0_0_1.subfields.IProcess;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressure;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IProcess_water_differential_pressure_sensor_1 extends IField{

	public IRI iri();

    public void addComposedOfDifferential (IDifferential parameter);

	public Set<IDifferential> getComposedOfDifferential();

    public void addComposedOfPressure (IPressure parameter);

	public Set<IPressure> getComposedOfPressure();

    public void addComposedOfProcess (IProcess parameter);

	public Set<IProcess> getComposedOfProcess();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}