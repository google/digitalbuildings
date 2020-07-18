package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IPowerfactor;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IPowerfactor_sensor extends IField{

	public IRI iri();

    public void addComposedOfPowerfactor (IPowerfactor parameter);

	public Set<IPowerfactor> getComposedOfPowerfactor();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}