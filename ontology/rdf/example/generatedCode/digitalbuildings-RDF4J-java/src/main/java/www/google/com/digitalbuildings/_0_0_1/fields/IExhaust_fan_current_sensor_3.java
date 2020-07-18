package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IExhaust;
import www.google.com.digitalbuildings._0_0_1.subfields.IFan;
import www.google.com.digitalbuildings._0_0_1.subfields.ICurrent;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IExhaust_fan_current_sensor_3 extends IField{

	public IRI iri();

    public void addComposedOfCurrent (ICurrent parameter);

	public Set<ICurrent> getComposedOfCurrent();

    public void addComposedOfExhaust (IExhaust parameter);

	public Set<IExhaust> getComposedOfExhaust();

    public void addComposedOfFan (IFan parameter);

	public Set<IFan> getComposedOfFan();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}